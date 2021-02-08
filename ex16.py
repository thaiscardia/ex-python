"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo."""
from math import radians, sin, cos, tan
a = int(input("Qual o ângulo de seu triângulo?"))
rad = radians(a)

print("O seno é {:.4f}, o cosseno é {:.4f} e a tangente é {:.4f}".format(sin(rad), cos(rad), tan(a)))
