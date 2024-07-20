css = '''
<style>
.chat-message {
    padding: 0.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 3%;
}
.chat-message .avatar img {
  max-width: 41px;
  max-height: 41px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 200%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.shutterstock.com/image-vector/cute-chat-bot-smiling-flat-260nw-2175518705.jpg" style="max-height: 41px; max-width: 41px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://static.vecteezy.com/system/resources/previews/019/879/186/non_2x/user-icon-on-transparent-background-free-png.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
