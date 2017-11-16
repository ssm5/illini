from app.models import *


broad_tags_string = """Academic
Fun
Sports
Greek Life"""

specific_tags_string = """Honorary < academic
International
Political < academic
Religious
Student Government < academic
Arts
Cultural
All-women
Philanthropy
Graduate"""

niche_tags_string = """African American < cultural
Asian American < cultural
Disability < philanthropy
Deaf < disability
Blind < disability
Arabian < cultural
Armenian < cultural
Indian < cultural
Bangladeshi < cultural
Filipino < cultural
Bengali < cultural
Yoga < sports
Ballet < sports, dance
Assyrian < cultural
Chorus < arts, music
A capella < chorus
Brazilian < cultural
Dance < sports, fun
Chinese < cultural
Minority < cultural
LGBTQ
Korean < cultural
Greek < cultural
Beauty
Hindu < cultural
Immigrants < cultural
Iranian < cultural
Jordanian < cultural
Lao < cultural
Latino < cultural
Malaysian < cultural
Mexican < cultural
Business < academic
Mongolian < cultural
Multi-ethnic < cultural
Japanese < cultural
Native American < cultural
Peruvian < cultural
Phillipino < cultural
Polish < cultural
Russian < cultural
South Asian < cultural
Taiwanese < cultural
Debate < academic
Turkish < cultural
Vietnamese < cultural
Music < arts
Design < arts
History < academic
Crafts < fun
Bollywood < fun
Photography < arts
Writing < academic
Theatre < arts
Folk
Hip-hop < sports
Guitar < music
Bhangra < cultural
Magic < fun
Cinema < fun
Latin < cultural
Yearbook
Western < cultural
Drawing < arts
Band < music
Muslim < cultural, religious
Comedy < fun
Videography < arts
Radio
Acting < arts
Film < arts
Improv < arts
Fashion < arts
Magazine
Mentorship < academic
All-male
Gymnastics < sports
Self defense < sports
Badminton < sports
Hockey < sports
Judo < sports
Aquatic sports < sports
Swimming < sports
Table Tennis < sports
Firearms < fun
Lacrosse < sports
Baseball < sports
Rowing < sports
Rugby < sports
Frisbee < sports
Volleyball < sports
Karate < sports
Skating < sports
Triathlon < sports
Hockey < sports
Basketball < sports
Softball < sports
Archery < sports
Trivia < academic, fun
Meditation < health
Games < fun
Martial arts < sports
Tricking < sports
Fencing < sports
Tennis < sports
Fitness < sports
Cross-country < sports
Extreme sports < sports
Board games < sports
Chess < sports
Video games < fun
Weightlifting < sports
Billiards < sports
Fishing < sports
Cycling < sports
Golf < sports
Technology < academic
Racing < sports
Handball < sports
Juggling < sports
Cycling < sports
Longboarding < sports
Racquetball < sports
Quidditch < sports
Card games
Soccer < sports
Sculling < sports
Sailing < sports
Skiing < sports
Snowboarding < sports
Spikeball < sports
Football < sports
Adventure < fun
Squash < sports
Paintball < sports
Track and field < sports
Robotics < academic
Accounting < academic
Security < academic
Environment
Science < academic
Chemistry < academic
Leadership < academic
Agriculture < academic
Advertising < academic
Aeronautics < academic
Engineering < academic
Marketing < academic
Medical < academic
Biology < academic
Civil engineering < academic
Mechanical engineering < academic
Computer science < academic
Trading < academic
Food
Entrepreneurship < academic
Innovation < academic
Poetry < academic
Christian < religious
Software development < academic
Networking < academic
Animals < fun
Careers < academic
Law < academic
Investment < academic
Construction management < academic
Business fraternity < academic, business
Economics < academic
Urban Planning < academic
Policy < academic
Entomology < academic
Computer engineering < academic
Finance < academic
Health < academic
Ecology < academic
Human development
Nutrition < academic
Advising < academic
Cars < fun
Statistics < academic
Physics < academic
Consulting < academic
Neuroscience < academic
Space < academic
Solar < academic
Disease < academic
Transportation
Interdisciplinary < academic
Kinesiology < academic
Liberal arts < academic
Mind and body < health
Materials Science < academic
Journalism < academic
Speech < academic
Mathematics < academic
Philosophy < academic
Sex < health
Education < academic
Nursing < academic
Veterinarians
Anime < fun
Astronomy < academic
Saudi < cultural
Republican < political
Democratic < political
Libertarian < political
Progressive < political
Socialist < political
Baptist < religious
Catholic < religious
Presbyterian < religious
Jewish < religious
Buddhist < religious
Lutheran < religious
Sikh < religious
Vedanta < religious
Residence hall
Equality < political
Foster < philanthropy
ROTC
STEM < academic"""


taglines = broad_tags_string.split("\n")
for line in taglines:
    arr = line.split(' < ')
    tag = arr[0]
    obj, created = Tag.objects.get_or_create(name=tag, breadth='B')
    if created:
        print('Added broad tag:', obj)

taglines = specific_tags_string.split("\n")
for line in taglines:
    arr = line.split(' < ')
    tag = arr[0]
    obj, created = Tag.objects.get_or_create(name=tag, breadth='S')
    if created:
        print('Added specific tag:', obj)

taglines = niche_tags_string.split("\n")
for line in taglines:
    arr = line.split(' < ')
    tag = arr[0]
    obj, created = Tag.objects.get_or_create(name=tag, breadth='N')
    if created:
        print('Added niche tag:', obj)

taglines = (broad_tags_string + '\n' + specific_tags_string + '\n' + niche_tags_string).split('\n')
for line in taglines:
    print(tag.parents.all().count())
    if len(arr) > 1:
        tag_string = arr[0]
        tag = Tag.objects.get(name=tag_string)
        parent_strings = arr[1].split(', ')
        # print(tag.parents.all().count())
        # tag.parents.clear()
        for parent_string in parent_strings:
            parent = Tag.objects.get(name__iexact=parent_string)
            # print(parent.__dict__)
            tag.parents.add(parent)
            print('Added', parent_string, 'as parent to', tag_string)

# tag1 = Tag.objects.get(name='Academic')
# tag2 = Tag.objects.get(name='Accounting')
#
# tag1.parents.clear()
# tag2.parents.clear()
# print("Before:")
# print(tag1.breadth)
# print("Tag1 has these parents:", tag1.parents.all())
# print("Tag2 has these parents:", tag2.parents.all())
#
# tag2.parents.add(tag1)
# print("After:")
# print("Tag1 has these parents:", tag1.parents.all())
# print("Tag2 has these parents:", tag2.parents.all())
#
# tag1.parents.clear()
# print("Lastly:")
# print("Tag1 has these parents:", tag1.parents.all())
# print("Tag2 has these parents:", tag2.parents.all())
