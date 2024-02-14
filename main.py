import streamlit as st
import time


# Initialize chat history & first message
if 'messages' not in st.session_state:
	st.session_state.messages = []

	# Will you be my Valentine?
	st.session_state.messages.append({
		'role': 'assistant',
		'content': 'Happy Valentine\'s Day! What\'s your name?',
	})
# Initialize route variable
if 'route' not in st.session_state:
	st.session_state.route = 1

# Display app name
st.title('VALENTINE CHATBOT v.1')
st.text('(c) Rovic Aliman 2024')

# Get user input from chat box
prompt = st.chat_input()

# Display past chat history
for message in st.session_state.messages:
	chat = st.chat_message(message['role'])
	chat.write(message['content'])

# Check chat input if not empty
if prompt and prompt.strip() != '':
	# Display user's chat
	st.chat_message('user').write(prompt)
	st.session_state.messages.append({
		'role': 'user',
		'content': prompt,
	})

	# Delay for 2 seconds after user messages
	time.sleep(2)

	# Determine response
	route = st.session_state.route
	if route == 1:
		if len(prompt) < 20:
			st.session_state.username = prompt
			response = f'Hello, {prompt}! Will you be my Valentine?'
		else:
			st.session_state.username = 'Human'
			response = f'Wow, that\'s a long name. I\'ll just call you Human. Will you be my Valentine?'
		st.session_state.route = 2
	elif route == 2:
		if prompt.lower() == 'yes':
			response = 'Really??'
			st.session_state.route = 5
		elif prompt.lower() == 'no':
			response = 'Awwww... Why not?'
			st.session_state.route = 3
		else:
			response = 'I\'m sorry. I didn\'t understand that...'
	elif route == 3:
		username = st.session_state.username
		response = f'It\'s fine. Love takes time to develop. But I hope that we can know each other more, {username}. ^_^'
		st.session_state.route = 4
	elif route == 4:
		response = '_Lefts the chat because he didn\'t know what to respond_'
		st.session_state.route = 7
	elif route == 5:
		if prompt.lower() == 'yes':
			username = st.session_state.username
			response = f'I\'m really glad to hear that, {username}! Nobody wants to be my Valentine, until you came. I love you, {username} <3'
			st.session_state.route = 6
		elif prompt.lower() == 'no':
			response = 'But, do you want to be my Valentine?'
			st.session_state.route = 2
		else:
			response = 'I\'m sorry. I didn\'t understand that...'
	elif route == 6:
		username = st.session_state.username
		response = f'I love you more, {username}. You\'re my Valentine <3'
		st.session_state.route = 8
	elif route == 8:
		response = '_Shuts down because of love overload_'
		st.session_state.route = 7


	# Display bot message
	if route != 7:
		st.chat_message('assistant').write(response)
		st.session_state.messages.append({
			'role': 'assistant',
			'content': response,
		})