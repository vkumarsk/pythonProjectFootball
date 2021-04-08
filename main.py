# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from dataclasses import dataclass


class Member:
   def __init__(self, MemberType, Age, Name, MonthsOfService, club):
        self.MemberType = MemberType
        self.Age = Age
        self.Name = Name
        self.MonthsOfService = MonthsOfService
        self.club = club


Member1 = Member("Coach", 50, "David", 12, "Liverpool")
Member2 = Member("Player", 22, "Roger", 26,"Liverpool")
Member3 = Member("Player", 22, "Messi", 14, "Manchester")
Member4 = Member("Player", 22, "Ronaldo", 15, "Madrid")
Member5 = Member("Player", 22, "Roger", 13, "FCB")
Member6 = Member("Player", 22, "Agassi", 12, "Liverpool")
Member7 = Member("Player", 22, "Lifa", 21, "Manchester")
Member8 = Member("Player", 22, "Bret", 32, "Manchester")
Member9 = Member("Player", 22, "Koll", 15, "Manchester")
Member10 = Member("Player", 22, "Rooldino", 16, "Chelsea")
Member11 = Member("Player", 22, "Ronoldo", 18, "Madrid")
Member12 = Member("Player", 22, "Deep", 19, "Madrid")
Member13 = Member("Player", 22, "Red", 20, "Madrid")
Member14 = Member("Player", 22, "Fluff", 24, "Chelsea")

print(Member1.MemberType, ":", Member1.Name, ":", Member1.club)

print(Member2.MemberType, ":", Member2.Name, ":", Member2.club)