# Author - Richa Sharma

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json

class RoomConsumer(AsyncWebsocketConsumer):
	
	async def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['roomId']
		self.room_group_name = 'room_%s' %  self.room_name
		print(self.room_group_name) 

		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)
		
		await self.accept()

		
	async def disconnect(self,close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)
		
	async def receive(self , text_data):
		print(text_data)
		await self.channel_layer.group_send(
			self.room_group_name,{
				'type' : 'run_game',
				'payload' : text_data
			}
		)
		
	
	def run_game(self , event):
		data = event['payload']
		data = json.loads(data)

		self.send(text_data= json.dumps({
			'payload' : data['data']
		}))        