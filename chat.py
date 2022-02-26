
from twitter_scraper import username
import numpy as np
import re
from test_model import encoder_model, decoder_model, num_decoder_tokens, num_encoder_tokens, input_features_dict, target_features_dict, reverse_target_features_dict, max_decoder_seq_length, max_encoder_seq_length

class ChatBot():
    negative_commands = ["bye", "no", "exit"]
    exit_commands = ["bye", "goodbye", "exit", "see ya"]
    def scrape_user(self):
        username = input("Enter the twitter handle of the user you want to converse with: ")
        return username

    def start_chat(self):
        user_input = input(f"Hi, I'm a chatbot trained on dialog from {username}. Would you like to chat with me?\n")
        for command in self.negative_commands:
            if command in user_input:
                return
        while not self.make_exit(user_input):
            user_input = input(self.generate_response(user_input))

    def make_exit(self, user_input):
        for command in self.exit_commands:
            if command in user_input:
                print("Okay bye!")
                return True
        return False

    def string_to_matrix (self, user_input):
        tokens = re.findall(r"[\w']+|[^\s\w]", user_input)
        user_input_matrix = np.zeros(
        (1, max_encoder_seq_length, num_encoder_tokens),
        dtype='float32')
        for timestep, token in enumerate(tokens):
            if token in input_features_dict:
                user_input_matrix[0, timestep, input_features_dict[token]] = 1.
        return user_input_matrix

    def generate_response(self, user_input):
        input_matrix = self.string_to_matrix(user_input)
        states_value = encoder_model.predict(input_matrix)

        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, target_features_dict['<START>']] = 1.

        decoded_sentence = ''

        stop_condition = False
        while not stop_condition:
            output_tokens, hidden_state, cell_state = decoder_model.predict(
            [target_seq] + states_value)

            sampled_token_index = np.argmax(output_tokens[0, -1, :])
            sampled_token = reverse_target_features_dict[sampled_token_index]
            decoded_sentence += " " + sampled_token

            if (sampled_token == '<END>' or len(decoded_sentence) > max_decoder_seq_length):
                stop_condition = True

            target_seq = np.zeros((1, 1, num_decoder_tokens))
            target_seq[0, 0, sampled_token_index] = 1.

            states_value = [hidden_state, cell_state]

            decoded_sentence = decoded_sentence.replace("<START>", "").replace("<END>", "").replace("RT","")
        decoded_sentence += ": "
        return decoded_sentence

bot = ChatBot()
bot.start_chat()