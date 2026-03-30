import random

easy_questions = [
    {"question": "What is the name of the only character who resisted the temptation of the One Ring?", "options": ["Samwise Gamgee", "Tom Bombadil", "Gandalf", "Pippin Took", "Aragorn"], "answer": "Tom Bombadil", "hint": "A figure that was introduced The Fellowship of the Ring."},

    {"question": "What is the name of Gandalf's horse in The Two Towers and The Return of the King?", "options": ["Pony", "Krom", "Snowflake", "Shadowfax", "Lightbearer"], "answer": "Shadowfax", "hint": "The lord of all horses, incredibly fast and intelligent."},

    {"question": "In Minas Tirith, who carries the wounded King Théoden from the battlefield during the Battle of the Pelennor Fields?", "options": ["Aragorn", "Merry", "Gandalf", "Faramir", "Éowyn"], "answer": "Éowyn", "hint": "A noble of Rohan, central to the Battle of the Pelennor Fields."},

    {"question": "What is the Arkenstone also known as?", "options": ["The White Gem of Gondor", "The Stone of Erebor", "The Jewel of Durin", "The Heart of the Mountain", "The King's Diamond"], "answer": "The Heart of the Mountain", "hint": "Thorin Oakenshield's most prized treasure, hidden deep within Erebor."},

    {"question": "Who originally owned the sword Sting before Bilbo?", "options": ["Thorin Oakenshield", "Elrond", "An Elven king of Gondolin", "Aragorn", "Dáin Ironfoot"], "answer": "An Elven king of Gondolin", "hint": "Its origin is from the First Age, revealed when Bilbo visits Rivendell in the Hobbit."},

    {"question": "What gift does Galadriel give Frodo in Lothlórien?", "options": ["An Elven cloak", "A silver horn", "A rope", "A star of Eärendil", "A sword"], "answer": "A star of Eärendil", "hint": "Something that will help him in darkness, which he first uses in The Two Towers, even though it was introduced in The Fellowship of the Ring."},

    {"question": "What do the beacons of Gondor signal?", "options": ["Victory over Mordor", "The crowning of the king", "A call for aid from Gondor", "The fall of Minas Tirith", "The return of Gandalf"], "answer": "A call for aid from Gondor", "hint": "It happened in the Return of the King and in the movie different characters set it on fire and see and deliver a message."},

    {"question": "Who frees Théoden from Saruman's influence?", "options": ["Aragorn", "Gandalf", "Éomer", "Gríma Wormtongue", "Legolas"], "answer": "Gandalf", "hint": "Character who 'dies' in the Fellowship of the Ring."},

    {"question": "What kind of creature is Gollum originally?", "options": ["Hobbit", "Man", "Dwarf", "Goblin", "Elf"], "answer": "Hobbit", "hint": "While he was named Sméagol, before he was transformed by the power of the One Ring."},

    {"question": "Where did Saruman die?", "options": ["Isengard", "Mordor", "Gondor", "Shire", "Rohan"], "answer": "Shire", "hint": "In the book he is killed in the different place then in the movies."},
    
    {"question": "What is the name of Frodo's loyal gardener and companion?", "options": ["Pippin Took", "Samwise Gamgee", "Meriadoc Brandybuck", "Bilbo Baggins", "Rosie Cotton"], "answer": "Samwise Gamgee", "hint": "He carries Frodo up Mount Doom."},

    {"question": "What is the name of the dark lord in The Lord of the Rings?", "options": ["Saruman", "Sauron", "Melkor", "Gothmog", "Denethor"], "answer": "Sauron", "hint": "He created the One Ring."},

    {"question": "What race is Legolas?", "options": ["Man", "Elf", "Dwarf", "Hobbit", "Wizard"], "answer": "Elf", "hint": "He has excellent eyesight and hearing."},

    {"question": "What is the name of the volcano where the One Ring is destroyed?", "options": ["Mount Doom", "Lonely Mountain", "Mount Gundabad", "Orodruin Peak", "Ash Mountain"], "answer": "Mount Doom", "hint": "It is located in Mordor."},

    {"question": "Who is the rightful king of Gondor?", "options": ["Boromir", "Faramir", "Aragorn", "Theoden", "Elrond"], "answer": "Aragorn", "hint": "He is also known as Strider."},

    {"question": "What creature says 'My precious'?", "options": ["Smaug", "Gollum", "Treebeard", "Saruman", "Shelob"], "answer": "Gollum", "hint": "He was once called Sméagol."},

    {"question": "What is the name of the inn where Frodo meets Aragorn?", "options": ["The Green Dragon", "The Golden Perch", "The Prancing Pony", "The Silver Harp", "The Red Dragon"], "answer": "The Prancing Pony", "hint": "It is located in Bree."},

    {"question": "What type of creature is Gimli?", "options": ["Elf", "Hobbit", "Dwarf", "Man", "Orc"], "answer": "Dwarf", "hint": "He is the son of Glóin."},

    {"question": "What is the name of Frodo's uncle?", "options": ["Otho Baggins", "Bilbo Baggins", "Drogo Baggins", "Bungo Baggins", "Fosco Baggins"], "answer": "Bilbo Baggins", "hint": "He found the One Ring in The Hobbit."},

    {"question": "Which group is formed to destroy the One Ring?", "options": ["The Council of Elrond", "The White Council", "The Fellowship of the Ring", "The Nine Walkers", "The Rangers"], "answer": "The Fellowship of the Ring", "hint": "It consists of nine members."}]

extra_questions = [
    {"question": "Who forged the Silmarils?", "options": ["Thingol", "Melkor", "Tulkas", "Elrond", "Fëanor"], "answer": "Fëanor", "hint": "He was one of the greatest Elven craftsmen of the First Age."},

    {"question": "What is the tragic fate of Túrin Turambar?", "options": ["He becomes King of Gondor", "He marries Lúthien", "He is turned to stone", "He kills himself", "He becomes a Maia"], "answer": "He kills himself", "hint": "His life is marked by sorrow and doom."},

    {"question": "What city is hidden and later falls due to betrayal in the First Age?", "options": ["Minas Tirith", "Gondolin", "Rivendell", "Osgiliath", "Erebor"], "answer": "Gondolin", "hint": "This secret Elven city is betrayed from within."},

    {"question": "What is the name of the human hero who enters Angband and escapes alive?", "options": ["Túrin", "Húrin", "Beren", "Beregond", "Haldir"], "answer": "Beren", "hint": "He falls in love with Lúthien."},

    {"question": "Who is the mother of Elrond and Elros?", "options": ["Idril", "Lúthien", "Galadriel", "Celebrían", "Elwing"], "answer": "Elwing", "hint": "She possesses a Silmaril."},

    {"question": "What great enemy first corrupts Elves and Men in the legendarium?", "options": ["Sauron", "Ungoliant", "Morgoth", "Saruman", "Glaurung"], "answer": "Morgoth", "hint": "He is the original Dark Lord."},

    {"question": "Who becomes King of the Dúnedain in exile after the downfall of Númenor?", "options": ["Isildur", "Arvedui", "Elendil", "Círdan", "Tar-Meneldur"], "answer": "Elendil", "hint": "He later founds Arnor and Gondor."},

    {"question": "In Unfinished Tales, what race are the Drúedain?", "options": ["Elves", "Dwarves", "Men of the West", "Elves of the Woods", "Orcs"], "answer": "Men of the West", "hint": "They are mysterious forest-dwellers."},

    {"question": "Who first finds the One Ring after it is lost by Isildur?", "options": ["Bilbo", "Déagol", "Sméagol", "Sauron", "Lurtz"], "answer": "Déagol", "hint": "He discovers it while fishing."},

    {"question": "What is the name of the Dark Lord defeated by the Last Alliance?", "options": ["Morgoth", "Sauron", "Ungoliant", "Witch-king of Angmar", "Gothmog"], "answer": "Sauron", "hint": "He is defeated at the end of the Second Age."},

    {"question": "What are Telperion and Laurelin collectively known as?", "options": ["Mallorn", "Sacred Trees", "The Glowing Trees", "The White Trees", "The Two Trees"], "answer": "The Two Trees", "hint": "They gave light to Valinor before the Sun and Moon."},

    {"question": "Who was the father of Fëanor?", "options": ["Finarfin", "Maedhros", "Finwë", "Túrin", "Thingol"], "answer": "Finwë", "hint": "He was High King of the Noldor."},

    {"question": "What event led to the rebellion of the Noldor?", "options": ["A plague", "Death of Finwë", "The theft of the Silmarils", "War with Orcs", "Melkor's imprisonment"], "answer": "The theft of the Silmarils", "hint": "This act by Morgoth drove Fëanor to rebel."},

    {"question": "Who is the mother of Lúthien?", "options": ["Thingol", "Melian", "Elrond", "Galadriel", "Celebrían"], "answer": "Melian", "hint": "She is a Maia and Queen of Doriath."},

    {"question": "Where did Glaurung first emerge?", "options": ["Thangorodrim", "Mount Doom", "Angband", "Ered Nimrais", "Mount Gundabad"], "answer": "Angband", "hint": "The stronghold of Morgoth."},

    {"question": "Which region did the Noldor first reach after leaving Valinor?", "options": ["Gondor", "Beleriand", "Rohan", "Mordor", "Harad"], "answer": "Beleriand", "hint": "Most First Age events take place here."},

    {"question": "Which Vala guided Turgon to found Gondolin?", "options": ["Manwë", "Ulmo", "Aulë", "Oromë", "Mandos"], "answer": "Ulmo", "hint": "He is the Lord of Waters."},

    {"question": "What was the name of Aragorn's mother?", "options": ["Elwing", "Idril", "Galadriel", "Morwen", "Gilraen"], "answer": "Gilraen", "hint": "She raised him in Rivendell."},

    {"question": "What is the Sindarin name for Rivendell?", "options": ["Lothlórien", "Minas Tirith", "Edhellond", "Imladris", "Thranduil"], "answer": "Imladris", "hint": "It means 'Deep Dale of the Cleft.'"}, 

    {"question": "Who is the Lord of the Eagles that helps Thorin and Company?", "options": ["Huan", "Beren", "Gwaihir", "Landroval", "Radagast"], "answer": "Gwaihir", "hint": "He also rescues Gandalf."},

    {"question": "Which realm did Thranduil rule?", "options": ["Lothlórien", "Mirkwood", "Rivendell", "Gondor", "Dale"], "answer": "Mirkwood", "hint": "A great forest in northern Middle-earth."},

    {"question": "What is the name of Éowyn's brother?", "options": ["Théodred", "Faramir", "Éomer", "Boromir", "Denethor"], "answer": "Éomer", "hint": "He becomes King of Rohan."},

    {"question": "Which Vala is associated with craftsmanship and the creation of the Dwarves?", "options": ["Aulë", "Manwë", "Ulmo", "Yavanna", "Tulkas"], "answer": "Aulë", "hint": "He shaped the Dwarves from stone."},

    {"question": "Who is the Lady of Lórien who gifts cloaks to the Fellowship?", "options": ["Galadriel", "Arwen", "Melian", "Celebrían", "Finduilas"], "answer": "Galadriel", "hint": "One of the mightiest Elves remaining."},

    {"question": "What was the original language of the Dwarves?", "options": ["Sindarin", "Quenya", "Adûnaic", "Westron", "Khuzdul"], "answer": "Khuzdul", "hint": "It was kept secret from outsiders."},

    {"question": "Who were the parents of Elrond?", "options": ["Túrin and Morwen", "Thingol and Melian", "Celeborn and Galadriel", "Finwë and Míriel", "Eärendil and Elwing"], "answer": "Eärendil and Elwing", "hint": "They are tied to the fate of the Silmarils."},

    {"question": "Which Maia became the chief servant of Morgoth?", "options": ["Radagast", "Gandalf", "Saruman", "Sauron", "Ilmarë"], "answer": "Sauron", "hint": "He later becomes the Dark Lord of the Second and Third Ages."},

    {"question": "What is the name of the land where Men first awoke?", "options": ["Hildórien", "Aman", "Valinor", "Númenor", "Rhûn"], "answer": "Hildórien", "hint": "The eastern homeland of Men."},

    {"question": "What wolf bit off Beren's hand containing a Silmaril?", "options": ["Ungoliant", "Carcharoth", "Glaurung", "Draugluin", "Watcher in the Water"], "answer": "Carcharoth", "hint": "He was the great wolf of Angband."},

    {"question": "Who was the first King of Númenor?", "options": ["Elros", "Elrond", "Isildur", "Ar-Pharazôn", "Anárion"], "answer": "Elros", "hint": "He chose the fate of Men."},

    {"question": "Who was Morgoth's chief lieutenant?", "options": ["Gothmog", "Sauron", "Ungoliant", "Azog", "Bolg"], "answer": "Sauron", "hint": "He later rises as the Dark Lord."},

    {"question": "Who becomes King of Gondor at the end of the War of the Ring?", "options": ["Boromir", "Faramir", "Aragorn", "Théoden", "Denethor"], "answer": "Aragorn", "hint": "He is crowned after the fall of Sauron."},

    {"question": "Who sacrificed his life in Sauron's dungeon to save Beren?", "options": ["Huan", "Thingol", "Carcharoth", "Finrod", "Maedhros"], "answer": "Finrod", "hint": "An Elven king and friend of Men."},

    {"question": "What is the name of the mountain where Smaug dwelt?", "options": ["Caradhras", "Mount Gram", "Erebor", "Thangorodrim", "Mindolluin"], "answer": "Erebor", "hint": "Also called the Lonely Mountain."},

    {"question": "Who was the captain of the Nazgûl?", "options": ["Khamûl", "The Mouth of Sauron", "Gríma Wormtongue", "The Witch-king of Angmar", "Saruman"], "answer": "The Witch-king of Angmar", "hint": "He leads the Ringwraiths."},

    {"question": "Who taught Aragorn healing and lore in Rivendell?", "options": ["Gandalf", "Radagast", "Elrond", "Galadriel", "Faramir"], "answer": "Elrond", "hint": "Lord of Imladris."},

    {"question": "What creatures does Bilbo fight in Mirkwood?", "options": ["Shelob", "Ungoliant", "Giant spiders", "Aragog", "Wargs"], "answer": "Giant spiders", "hint": "They capture the dwarves in the forest."},

    {"question": "Who becomes King under the Mountain after Thorin Oakenshield?", "options": ["Balin", "Fíli", "Kíli", "Dáin Ironfoot", "Glóin"], "answer": "Dáin Ironfoot", "hint": "He leads after the Battle of Five Armies."},

    {"question": "What is the name of Éomer's sword?", "options": ["Herugrim", "Andúril", "Glamdring", "Gúthwinë", "Sting"], "answer": "Gúthwinë", "hint": "A sword of the Rohirrim."},

    {"question": "What was the name of the great island kingdom of Men that sank beneath the sea?", "options": ["Gondor", "Harad", "Rhûn", "Umbar", "Númenor"], "answer": "Númenor", "hint": "Its downfall came from defying the Valar."},
    
    {"question": "Who was the father of Thingol, king of Doriath?", "options": ["Finwë", "Olwë", "Elwë", "Ingwë", "Círdan"], "answer": "Olwë", "hint": "He was the leader of the Teleri who remained in Aman."},

    {"question": "What was the name of Finrod Felagund's underground stronghold?", "options": ["Menegroth", "Nargothrond", "Gondolin", "Angband", "Tol Sirion"], "answer": "Nargothrond", "hint": "It was inspired by Thingol's halls in Doriath."},

    {"question": "Who betrayed Gondolin to Morgoth?", "options": ["Maeglin", "Eöl", "Curufin", "Celegorm", "Caranthir"], "answer": "Maeglin", "hint": "He desired Idril and revealed the city's location."},

    {"question": "What was the name of the river that formed the eastern boundary of Doriath?", "options": ["Sirion", "Gelion", "Esgalduin", "Narog", "Aros"], "answer": "Esgalduin", "hint": "Thingol's halls of Menegroth were built beside it."},

    {"question": "Who was the father of Gil-galad, the last High King of the Noldor?", "options": ["Fingon", "Finrod", "Orodreth", "Turgon", "Angrod"], "answer": "Orodreth", "hint": "This parentage is given in later versions of Tolkien's writings."},

    {"question": "What was the name of the fortress on Tol Sirion after Sauron captured it?", "options": ["Angband", "Barad-dûr", "Dol Guldur", "Tol-in-Gaurhoth", "Minas Morgul"], "answer": "Tol-in-Gaurhoth", "hint": "It means 'Isle of Werewolves'."},

    {"question": "Who was the wife of Tuor and mother of Eärendil?", "options": ["Idril", "Aredhel", "Lúthien", "Finduilas", "Celebrían"], "answer": "Idril", "hint": "She was the daughter of Turgon of Gondolin."},

    {"question": "What was the name of the forest where Eöl dwelt?", "options": ["Brethil", "Neldoreth", "Nan Elmoth", "Taur-nu-Fuin", "Region"], "answer": "Nan Elmoth", "hint": "A dark forest east of Doriath."},

    {"question": "Who led the Teleri who remained in Middle-earth and became the Sindar?", "options": ["Olwë", "Elwë", "Ingwë", "Finwë", "Thingol"], "answer": "Elwë", "hint": "He later became known as Thingol Greycloak."},

    {"question": "What was the name of the haven built at the mouths of the river Sirion?", "options": ["Alqualondë", "Mithlond", "Eglarest", "Havens of Sirion", "Vinyamar"], "answer": "Havens of Sirion", "hint": "It became a refuge after the fall of Gondolin and Doriath."}]

advanced_questions = [
    {"question": "What is the name of the great fortress in Hithlum held by Fingolfin's kin in the First Age?", "options": ["Himring", "Tol-in-Gaurhoth", "Nargothrond", "Gondolin", "Angband"], "answer": "Himring", "hint": "It was captured and held by Morgoth multiple times."},

    {"question": "Who was the eldest son of Fëanor?", "options": ["Maglor", "Maedhros", "Celegorm", "Caranthir", "Curufin"], "answer": "Maedhros", "hint": "He was captured by Morgoth and later rescued by his brothers."},

    {"question": "What are the names of the two great lamps created by the Valar before the Two Trees?", "options": ["Telperion and Laurelin", "Illuin and Ormal", "Vingilótë and Lorien", "Aulë and Yavanna", "Manwë and Tulkas"], "answer": "Illuin and Ormal", "hint": "They illuminated the world during the earliest ages."},

    {"question": "Which Maia was originally of good nature but later became the Dark Lord, serving Morgoth?", "options": ["Sauron", "Melian", "Olorin", "Aulë", "Ulmo"], "answer": "Sauron", "hint": "He was a Maia of Aulë who was corrupted by Morgoth."},

    {"question": "What was the original Elvish name of Gondolin?", "options": ["Turgon's City", "Nargothrond", "Ondolindë", "Hithlum", "Angband"], "answer": "Ondolindë", "hint": "It means 'The Rock of the Music of Water.'"},

    {"question": "Who was the Maia that protected Menegroth, the Thousand Caves of Doriath?", "options": ["Melian", "Finrod Felagund", "Thingol", "Maeglin", "Beleg"], "answer": "Melian", "hint": "She was a Maia who wove a protective enchantment over the kingdom."},

    {"question": "Which character is called the Hound of Valinor?", "options": ["Carcharoth", "Gothmog", "Beleg", "Huan", "Ancalagon"], "answer": "Huan", "hint": "He helps Beren and Lúthien in their quest for a Silmaril."},

    {"question": "What is the name of the spider that assisted Morgoth during the theft of the Silmarils?", "options": ["Shelob", "Aragog", "Kankra", "Ungoliant", "Mirkspider"], "answer": "Ungoliant", "hint": "She was the mother of all spiders and consumed endlessly due to hunger."},

    {"question": "What was the name of the river by which the Elves fled the destruction of Gondolin?", "options": ["Gelion", "Sirioneth", "Esgalduin", "Adurant", "Sirion"], "answer": "Sirion", "hint": "It flows from the northern mountains into Beleriand."},

    {"question": "Who was the Lord of the Balrogs of Morgoth?", "options": ["Azog", "Sauron", "Ungoliant", "Gothmog", "Thangorodrim"], "answer": "Gothmog", "hint": "He commanded in the Nirnaeth Arnoediad and Morgoth's wars."},

    {"question": "What is the name of the strongest dragon that destroyed three mountain peaks of Thangorodrim by falling on them?", "options": ["Smaug", "Glaurung", "Chrysophylax Dives", "Scatha", "Ancalagon the Black"], "answer": "Ancalagon the Black", "hint": "He was the mightiest of Morgoth's fire-drakes in the First Age."},

    {"question": "Which Edain hero sailed to Aman carrying a Silmaril?", "options": ["Tuor", "Eärendil", "Húrin", "Turgon", "Finarfin"], "answer": "Eärendil", "hint": "He became the Evening Star after pleading to the Valar."},

    {"question": "Who was the captain of the host that defended Gondolin during the Fall?", "options": ["Glorfindel", "Turgon", "Ecthelion", "Maeglin", "Finrod"], "answer": "Ecthelion", "hint": "He sacrificed himself facing Gothmog, Lord of the Balrogs."},

    {"question": "Which Noldorin elf forged the sword Anglachel from a meteorite?", "options": ["Fëanor", "Finrod", "Eöl", "Maeglin", "Celegorm"], "answer": "Eöl", "hint": "He was known as the Dark Elf of Nan Elmoth."},

    {"question": "What was the name of the first sword reforged from the shards of Narsil?", "options": ["Andúril", "Gúthwinë", "Ringil", "Herugrim", "Sting"], "answer": "Andúril", "hint": "It was reforged for the heir of Isildur."},

    {"question": "Who was the first to challenge Morgoth directly and survive the encounter?", "options": ["Túrin Turambar", "Fëanor", "Finrod Felagund", "Fingolfin", "Beren"], "answer": "Fingolfin", "hint": "He rode alone to Angband and wounded Morgoth seven times."},

    {"question": "Which Edain hero was cursed to suffer doom for generations by Morgoth?", "options": ["Beren", "Húrin", "Tuor", "Eärendil", "Tuor"], "answer": "Húrin", "hint": "His family became infamous in the tragedies of the First Age."},

    {"question": "What was the secret name of the sea-king of Númenor?", "options": ["Ar-Adûnakhôr", "Tar-Meneldur", "Ar-Pharazôn", "Tar-Calmacil", "Ar-Zimrathôn"], "answer": "Tar-Calmacil", "hint": "He ruled Númenor during its height before its decline."},

    {"question": "Which dragon guarded the treasure of the Noldor in the First Age?", "options": ["Glaurung", "Smaug", "Ancalagon the Black", "Scatha", "Chrysophylax Dives"], "answer": "Glaurung","hint": "Known as the Father of Dragons and enemy of Túrin."},

    {"question": "Who was the Lord of Dor-lómin and father of Túrin Turambar?", "options": ["Húrin", "Huor", "Thingol", "Beren", "Finrod"], "answer": "Húrin", "hint": "He was taken prisoner by Morgoth during the Nirnaeth Arnoediad."},
    
    {"question": "What was the name of the hill where Finwë was slain by Morgoth?", "options": ["Taniquetil", "Formenos", "Ezellohar", "Túna", "Valmar"], "answer": "Formenos", "hint": "It was Fëanor's stronghold in exile in Aman."},

    {"question": "Who was the second son of Fingolfin and brother of Turgon?", "options": ["Fingon", "Finrod", "Angrod", "Aegnor", "Orodreth"], "answer": "Fingon", "hint": "He rescued Maedhros from Thangorodrim."},

    {"question": "What was the name of the sword of Beleg Strongbow?", "options": ["Angrist", "Anglachel", "Gurthang", "Orcrist", "Ringil"], "answer": "Anglachel", "hint": "It was later reforged and renamed Gurthang."},

    {"question": "Who was the lord of the Falas and friend of the Noldor?", "options": ["Círdan", "Thingol", "Olwë", "Eöl", "Denethor"], "answer": "Círdan", "hint": "A shipwright who later aids in the War of the Ring."},

    {"question": "What was the name of the battle in which Fingon and Maedhros attempted to defeat Morgoth but were betrayed?", "options": ["Dagor Bragollach", "Nirnaeth Arnoediad", "Dagor-nuin-Giliath", "War of Wrath", "Battle of Sudden Flame"], "answer": "Nirnaeth Arnoediad", "hint": "Also called the Battle of Unnumbered Tears."},

    {"question": "Who was the father of Celebrimbor, the forger of the Rings of Power?", "options": ["Curufin", "Celegorm", "Caranthir", "Maglor", "Maedhros"], "answer": "Curufin", "hint": "He was one of the sons of Fëanor."},

    {"question": "What was the name of the river that flowed through Nargothrond?", "options": ["Narog", "Sirion", "Gelion", "Aros", "Esgalduin"], "answer": "Narog", "hint": "Its caves housed Finrod's realm."},

    {"question": "Which Vala pronounced the Doom of Mandos upon the Noldor?", "options": ["Mandos", "Manwë", "Ulmo", "Tulkas", "Aulë"], "answer": "Mandos", "hint": "Also known as Námo, the Doomsman of the Valar."},

    {"question": "What was the name of the hidden vale where Gondolin was built?", "options": ["Tumladen", "Nan Elmoth", "Brethil", "Dor-lómin", "Hithlum"], "answer": "Tumladen", "hint": "A secret valley surrounded by the Encircling Mountains."},

    {"question": "Who was the captain of the guards of Thingol and friend of Túrin?", "options": ["Beleg", "Mablung", "Saeros", "Eöl", "Gwindor"], "answer": "Beleg", "hint": "He was known as Strongbow."}]

def get_random_questions():
    return random.choice(easy_questions)

def get_random_basic():
    return random.choice(extra_questions)

def get_random_extra():
    return random.choice(advanced_questions)