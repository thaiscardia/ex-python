"""Faça um programa que abra e reproduza o áudio de um arquivo MP3"""
import pygame #biblioteca voltada para jogos em python
pygame.init()
pygame.mixer.music.load('love-you-to-death.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass