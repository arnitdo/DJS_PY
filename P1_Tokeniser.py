some_para = """Bacon ipsum dolor amet strip steak tri-tip pork chop tongue, ball tip shank tenderloin. Shankle cow hamburger salami, turkey strip steak short loin pastrami drumstick. Buffalo cow meatloaf pork chop landjaeger. Short loin flank salami cupim swine venison, andouille ribeye ham hock. Buffalo tail salami drumstick spare ribs short loin. Spare ribs tri-tip picanha, boudin hamburger rump sirloin.

Boudin shankle pork belly, salami ham hock flank pork chop filet mignon short loin andouille burgdoggen. Venison boudin picanha filet mignon shank salami kevin kielbasa cupim swine tenderloin. Bresaola short loin pastrami picanha boudin kielbasa swine ham hock fatback. Pig ham corned beef, buffalo shankle picanha pancetta andouille meatball pork loin rump bresaola beef ribeye porchetta. Chicken frankfurter shankle swine, ham hock pig short ribs ribeye landjaeger venison capicola pastrami meatloaf burgdoggen meatball. Meatloaf prosciutto t-bone, meatball drumstick leberkas alcatra buffalo pork chop filet mignon beef shank shoulder ribeye. Prosciutto ball tip sausage, swine ribeye ham hock meatball cupim turducken spare ribs ham rump capicola bacon.

Turkey corned beef shank tail biltong. Sirloin kevin ground round, boudin shank t-bone turkey burgdoggen pork chop strip steak beef ribs picanha bresaola short loin flank. Pig tongue short ribs strip steak pastrami brisket rump chuck picanha beef ribs. Buffalo fatback tenderloin chicken rump.

Tenderloin pancetta prosciutto spare ribs, chuck alcatra venison meatball kielbasa ball tip pork tongue leberkas pork chop ham hock. Filet mignon sirloin pig strip steak meatball ham hock sausage venison capicola pork chop flank pancetta biltong buffalo prosciutto. Strip steak ground round chicken jerky burgdoggen spare ribs ribeye, kevin ham hock porchetta tongue tenderloin. Pork loin frankfurter hamburger, rump brisket shankle bacon salami. Ground round beef rump shankle, ham hock pancetta short ribs turducken alcatra.

Capicola brisket jerky, biltong prosciutto ball tip pork chop beef ribs chuck landjaeger ham. Venison burgdoggen meatloaf boudin, picanha meatball porchetta short ribs pig. Rump cow doner prosciutto shank porchetta chislic sirloin boudin. Shank meatball boudin, filet mignon jowl kevin short ribs pork chop pastrami biltong sirloin corned beef shoulder buffalo alcatra. Doner porchetta ball tip pig, ground round shankle drumstick chuck tri-tip pork loin alcatra sirloin short ribs. Flank bresaola tenderloin strip steak. Cow brisket ribeye corned beef drumstick ground round ham hock capicola rump swine meatball."""

for char_to_remove in ".,-;_\n\t":
    some_para = some_para.replace(char_to_remove, " ")
    
split_words = some_para.split(" ")

split_words = list(
    filter(
		lambda string: False if len(string) == 0 else True,
		split_words
	)
)

lowercase_words = list(
	map(
		lambda string: string.lower(),
		split_words
	)
)

word_map = dict()

for word in lowercase_words:
    word_map[word] = word_map.get(word, 0) + 1
    
print(word_map)	
