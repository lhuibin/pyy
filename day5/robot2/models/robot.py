#!/usr/bin/env python
# coding:utf-8
# 机器人具有联网功能，不知道的问题联网查询。
class Robot(object):

	def reply(sefl,msgClient):
		if 'hi' in msgClient or 'hello' in msgClient:
			msgReply = 'hello'
		elif 'how are you' in msgClient:
			msgReply = 'fine, thank you!'
		elif 'check msg' in msgClient:
			msgReply = 'We are message data:\n'
		else:
			msgReply = 'sorry, I am very young, I will learning hardly. when you ask me this question next time, I must be know the answer!'
		return msgReply
