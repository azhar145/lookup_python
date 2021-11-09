##from faker import Faker
##from faker.providers import internet
##
##fake = Faker()
##fake.add_provider(internet)
##
##print(fake.ipv4_private())
##


##
from faker import Faker
fake = Faker('en_US')

print(fake.name())
# 'Lucy Cechtelar'

print(fake.address())
print(fake.latitude(), fake.longitude()) 


##from faker import Faker 
##fake = Faker('en_US') 
##print (fake.email()) 
##print(fake.country()) 
##print(fake.name()) 
##print(fake.text()) 
##print(fake.latitude(), fake.longitude()) 
##print(fake.url()) 

##

##from faker import Faker
##fake = Faker(['it_IT', 'en_US', 'ja_JP'])
##for _ in range(10):
##    print(fake.name())

