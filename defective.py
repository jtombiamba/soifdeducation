#!/usr/bin/python

import os
import glob
import re
import sys

def get_elementary_list():
	
	insn_list = list()
	insn_specific_list = list()
	removal_list = list()
	insn_file = open('sandy_bridge_revect.csv', 'r')
	headline = insn_file.readline()
	headline.strip("\n")

	content = insn_file.readline()
	while len(content) > 0:
					content.strip("\n")
					insn_list.append(content)
					insn_specific_list.append(content.split(";", 1)[0])
					content = insn_file.readline()

	for j in insn_list:
					if re.search('^PCMPEQ/GT\s*B/W/D', j) != None:
							removal_list.append('PCMPEQ[BWD];'+j.split(";", 1)[1])
							removal_list.append('PCMPGT[BWD];'+j.split(";", 1)[1])

					elif re.search('CVT\(T\)\s+', j) != None:
							se = re.sub('\(T\)\s+', "[T]?", j)
							removal_list.append(se)

					elif re.search('CMPccSS/D', j) != None:
								removal_list.append(re.match('(\w*)CMP', j).group(1)+'CMPS[SD];'+j.split(";", 1)[1])

					elif re.search('PADD/SUB\(U,S\)B/W/D/Q', j) != None or re.search('PADD/SUB/\(U\)\(S\)B/W/D/Q', j) != None:
							removal_list.append('PADD[BWDQ];'+j.split(";", 1)[1])
							removal_list.append('PSUB[BWDQ];'+j.split(";", 1)[1])
							removal_list.append('PADDS[BW];'+j.split(";", 1)[1])
							removal_list.append('PSUBS[BW];'+j.split(";", 1)[1])
							removal_list.append('PADDUS[BW];'+j.split(";", 1)[1])
							removal_list.append('PSUBUS[BW];'+j.split(";", 1)[1])

					elif re.search('B/W/D', j) != None:
								se = re.sub('B/W/D', "[BWD]", j)
								removal_list.append(se)

					elif re.search('PHADD/SUB\(S\)W/D', j) != None:
								removal_list.append('PHADD[WD];'+j.split(";", 1)[1])
								removal_list.append('PHADDSW;'+j.split(";", 1)[1])
								removal_list.append('PHSUB[WD];'+j.split(";", 1)[1])
								removal_list.append('PHSUBSW;'+j.split(";", 1)[1])

					elif re.search('PMIN/MAXU/SD', j) != None:
								removal_list.append('PMIN[US]D;'+j.split(";", 1)[1])
								removal_list.append('PMAX[US]D;'+j.split(";", 1)[1])

					elif re.search('PMIN/MAXUB/SW', j) != None:
								removal_list.append('PMINUB;'+j.split(";", 1)[1])
								removal_list.append('PMINSW;'+j.split(";", 1)[1])
								removal_list.append('PMAXUB;'+j.split(";", 1)[1])
								removal_list.append('PMAXSW;'+j.split(";", 1)[1])

					elif re.search('UNPCKH/LPS/D', j) != None:
								removal_list.append(re.match('(\w*)UNPCK', j).group(1)+'UNPCK[HL]P[SD];'+j.split(";", 1)[1])

					elif re.search('MOVH/LPS/D', j) != None:
								removal_list.append(re.match('(\w*)MOV', j).group(1)+'MOV[HL]P[SD];'+j.split(";", 1)[1])

					elif re.search('PUNPCKH/LBW/WD/DQ', j) != None:
								removal_list.append(re.match('(\w*)PUNPCK', j).group(1)+'PUNPCK[HL]BW;'+j.split(";", 1)[1])
								removal_list.append(re.match('(\w*)PUNPCK', j).group(1)+'PUNPCK[HL]WD;'+j.split(";", 1)[1])
								removal_list.append(re.match('(\w*)PUNPCK', j).group(1)+'PUNPCK[HL]DQ;'+j.split(";", 1)[1])

					elif re.search('PMOVSX/ZX', j) != None:
								removal_list.append('PMOVSX'+re.search('ZX(\w+)', j).group(1)+";"+j.split(";", 1)[1])
								removal_list.append('PMOVZX'+re.search('ZX(\w+)', j).group(1)+";"+j.split(";", 1)[1])

					elif re.search('PACKSSWB/DW', j) != None:
								removal_list.append('PACKSSWB;'+j.split(";", 1)[1])
								removal_list.append('PACKSSDW;'+j.split(";", 1)[1])

					elif re.search('PAVGB/W', j) != None:
								removal_list.append('PAVG[BW];'+j.split(";", 1)[1])

					elif re.search('(\w*)AND/ANDN/OR/XORPS/PD', j) != None:
								removal_list.append(re.match('(\w*)AND/', j).group(1)+'ANDP[SD];'+j.split(";", 1)[1])
								removal_list.append(re.match('(\w*)AND/', j).group(1)+'ANDNP[SD];'+j.split(";", 1)[1])
								removal_list.append(re.match('(\w*)AND/', j).group(1)+'ORP[SD];'+j.split(";", 1)[1])
								removal_list.append(re.match('(\w*)AND/', j).group(1)+'XORP[SD];'+j.split(";", 1)[1])

					elif re.search('PSLL/RL/RAW/D/Q', j) != None:
								removal_list.append('PSLL[WDQ];'+j.split(";", 1)[1])
								removal_list.append('PSRL[WDQ];'+j.split(";", 1)[1])
								removal_list.append('PSRA[WDQ];'+j.split(";", 1)[1])

					elif re.search('PSLL/RLDQ', j) != None:
								removal_list.append('PS[RL]LDQ;'+j.split(";", 1)[1])

					elif re.search('MIN/MAX', j) != None:
								se = re.sub('MIN/MAX', "MIN", j)
								removal_list.append(re.sub('MIN/MAX', "MIN", j))
								removal_list.append(re.sub('MIN/MAX', "MAX", j))

					elif re.search('H/L', j) != None:
	 							se = re.sub('H/L', "[HL]", j)
								removal_list.append(se)

					elif re.search('L/H', j) != None:
								se = re.sub('L/H', "[LH]", j)
								removal_list.append(se)

					elif re.search('SS/SD/PS/PD', j) != None:
								removal_list.append(re.match('(.*)SS/SD/PS/PD', j).group(1)+'[SP][SD];'+j.split(";", 1)[1])

					elif re.search('(.*)S/D', j) != None:
							se = re.sub('S/D', "[SD]", j)
							removal_list.append(se)

					elif re.search('(.*)PS/PD', j) != None:
							se = re.sub('PS/PD', "P[SD]", j)
							removal_list.append(se)

					elif re.search('(.*)SS/PS', j) != None:
							se = re.sub('SS/PS', "[SP]S", j)
							removal_list.append(se)

					elif re.search('(.*)SD/PD', j) != None:
							se = re.sub('SD/PD', "[SP]D", j)
							removal_list.append(se)
			
					elif re.search('AESDEC, AESDECLAST, AESENC, AESENCLAST', j):
							removal_list.append('AESDEC;'+j.split(";", 1)[1])
							removal_list.append('AESDECLAST;'+j.split(";", 1)[1])
							removal_list.append('AESENC;'+j.split(";", 1)[1])
							removal_list.append('AESENCLAST;'+j.split(";", 1)[1])

					else:
							removal_list.append(j)	

	local_list = list()					
	for j in removal_list:
					local_insn = j.split(";", 1)[0]
					if re.search('\s', local_insn) != None:
									#print local_insn
									removal_list.append(local_insn.split(" ", 1)[0]+";"+j.split(";", 1)[1]) 		
									removal_list.append(local_insn.split(" ", 1)[1]+";"+j.split(";", 1)[1]) 		
									removal_list.remove(j)
	
	insn_list.sort()
	insn_specific_list.sort()

	insn_output = open('output.csv', 'w')
	insn_output_2 = open('output_2.csv', 'w')

	insn_output.write(headline)
	for i in insn_list:
					content = insn_output.write(i)

	for j in removal_list:
					content = insn_output_2.write(j)
					#content = insn_output_2.write('\n')

	insn_file.close()
	insn_output.close()
	insn_output_2.close()


def find_appropriate_line(my_line, agner_list):
	
	for i in agner_list:
					if re.search(my_line[0], i.split(";", i.count(";"))[0]) != None:
									return i
					return i				

def get_comparison():

	insn_input = open('sandy_bridge.csv', 'r')
	insn_list_to_compare = open('SDB_Results_port.csv', 'r')
	my_list = list()
	agner_list = list()
	
	headline = insn_list_to_compare.readline()
	headline.strip("\n")
 
	content = insn_list_to_compare.readline()
	while len(content) > 0:
					content.strip("\n")
					my_list.append(content.split(";", content.count(";")))
					content = insn_list_to_compare.readline()

	for agner_content in insn_input:
					agner_content.strip('\n')
					agner_list.append(agner_content.split(";", agner_content.count(";")))
					#agner_content = insn_input.readline()
	print('Instruction;Latency ratio;Throughput ratio;Uops ratio;Port_0(Agner value);Port_1(Agner value);Port_2(Agner value);Port_3(Agner value);Port_4(Agner value);Port_5(Agner value);')
	for i in my_list:
					for j in agner_list:
									regex = re.compile('%s'%j[0])
									if regex.match(i[0]) != None:
													insn_line = list()
													insn_line.append(i[0])
													try:
														k = float(i[1])
														insn_line.append(str(round(k / float(j[1].split('-')[0].replace(',','.')), 2)))
														b = float(i[2])
														insn_line.append(str(round(b / float(j[2].split('-')[0].replace(',','.')), 2)))
														c = float(i[3])
														k = float(j[3].split('-')[0].replace(',','.'))
														insn_line.append(str(c / k))

														port_list = list()
														if j[4] == 'x' and j[5] == 'x' and j[8] == 'x\n':
																		port_list.extend([str(round(k/3, 2)), str(round(k/3, 2)), str(round(k/3, 2))])
														elif j[4] == '' and j[5] == '' and j[8] == '\n':
																		port_list.extend(['', '', '']) 			
														elif j[4] == 'x' and j[5] == 'x':
																		port_list.extend([str(round(k/2, 2)), str(round(k/2, 2)), '0'])
														elif j[4] == 'x' and j[8] == 'x\n':
																		port_list.extend([str(k/2), '0', str(k/2)])
														elif j[5] == 'x' and j[8] == 'x\n':
																		port_list.extend(['0', str(k/2), str(k/2)])
														elif j[4] == '' and j[5] == '':
																		port_list.extend(['0', '0', j[8].split('\n')[0]])
														elif j[4] == '' and j[8] == '\n':
																		port_list.extend(['0', j[5], '0'])
														elif j[5] == '' and j[8] == '\n':
																		port_list.extend([j[4], '0', '0'])
														else:
																		port_list.extend([j[4], j[5], j[8].split('\n')[0]])				
															
														insn_line.extend([i[4]+'('+port_list[0]+')', i[5]+'('+port_list[1]+')', i[6]+'('+j[6]+')', i[7]+'('+j[6]+')', i[8]+'('+j[7]+')', i[9]+'('+port_list[2]+')'])
														for element in insn_line:
																		sys.stdout.write(element+';')
														sys.stdout.write('\n')				
													except ValueError:
														for element in insn_line:
																		sys.stdout.write(element+';')
														sys.stdout.write('\n')				
	
	insn_input.close()
	insn_list_to_compare.close()
	
def module_matching(z, prefetch_distance, file_input, file_output):

		reg_rank = 0			
		for line in file_input.readlines():
				offset = 0			
				for k in range(1,z):
						if re.search('vmovaps', line) != None:
								substring = re.sub('0\(', str(offset) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								offset = offset + 64
								reg_rank = reg_rank + 1

						elif re.search('vprefetch0 0\(', line) != None:
								substring = re.sub('0\(', str(prefetch_distance) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								prefetch_distance = prefetch_distance + 64

def instruction_repetition(new_file, where_to_prefetch):
	 
	file_input = open(new_file, 'r')
	file_output = open('temp.out', 'w')
	where_to_prefetch = int(where_to_prefetch)
	i = 0		
	j = 0		
	previous_line = ''
	for line in file_input.readlines():
			if re.search('vmovaps', line) != None:
					if re.search('vmovaps 0\(', line) != None:
						if re.search('vprefetch[01]', previous_line) != None:					
							file_output.write(previous_line)
							j = j + 1	
						file_output.write(line)	
						i = i + 1
					elif re.search('vmovaps \%', line) != None:
						if re.search('vprefetch[01]', previous_line) != None:
							file_output.write(re.sub('vprefetch', 'vprefetche', previous_line))
							j = j + 1
						file_output.write(line)
						i = i + 1					
			#elif re.search('vprefetch0', line) != None:
			#		file_output.write(line)	
			#		j = j + 1
			previous_line = line		
	
	file_input.close()
	file_output.close()

	file_input = open('temp.out', 'r')
	file_output = open('raw.s', 'w')
	file_output.write('.L6:\n')
	if i == 1:
		z = 33
		#module_matching(z, 1024, file_input, file_output)
		reg_rank = 0
		z = 33
		for line in file_input.readlines():
				offset = 0			
				prefetch_distance = where_to_prefetch
				for k in range(1,z):
						if re.search('vmovaps', line) != None:
								substring = re.sub('0\(', str(offset) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								offset = offset + 64
								reg_rank = reg_rank + 1

						elif re.search('vprefetch[01] 0\(', line) != None or re.search('vprefetche[01] 0\(', line) != None:
								substring = re.sub('0\(', str(prefetch_distance) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								prefetch_distance = prefetch_distance + 64
	elif i == 2:
		reg_rank = 0
		z = 17
		#module_matching(z, 1024, file_input, file_output)
 		for line in file_input.readlines():
 				offset = 0			
 				prefetch_distance = where_to_prefetch
 				for k in range(1,z):
 						if re.search('vmovaps', line) != None:
 								substring = re.sub('0\(', str(offset) + '(', line)		
 								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
 								#file_output.write(substring)
 								offset = offset + 64
 								reg_rank = reg_rank + 1
 
 						elif re.search('vprefetch[01] 0\(', line) != None or re.search('vprefetche[01] 0\(', line) != None:
 								substring = re.sub('0\(', str(prefetch_distance) + '(', line)		
 								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
 								#file_output.write(substring)
 								prefetch_distance = prefetch_distance + 64
	elif i == 3:
		reg_rank = 0
		z = 11
		#module_matching(z, 1024, file_input, file_output)
		for line in file_input.readlines():
				offset = 0			
				prefetch_distance = where_to_prefetch
				for k in range(1,z):
						if re.search('vmovaps', line) != None:
								substring = re.sub('0\(', str(offset) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								offset = offset + 64
								reg_rank = reg_rank + 1

						elif re.search('vprefetch[01] 0\(', line) != None or re.search('vprefetche[01] 0\(', line) != None:
								substring = re.sub('0\(', str(prefetch_distance) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								prefetch_distance = prefetch_distance + 64
	elif i == 4:
		reg_rank = 0
		z = 9
		#module_matching(z, 1024, file_input, file_output)
		for line in file_input.readlines():
				offset = 0			
				prefetch_distance = where_to_prefetch
				for k in range(1,z):
						if re.search('vmovaps', line) != None:
								substring = re.sub('0\(', str(offset) + '(', line)		
								file_output.write(re.sub('zmm[0-9]*','zmm' + str(reg_rank) ,substring))
								#file_output.write(substring)
								offset = offset + 64
								reg_rank = reg_rank + 1

						elif re.search('vprefetch[01] 0\(', line) != None or re.search('vprefetche[01] 0\(', line) != None:
								substring = re.sub('0\(', str(prefetch_distance) + '(', line)		
								file_output.write(substring)
								#file_output.write(substring)
								prefetch_distance = prefetch_distance + 64
	file_output.write('add $'+str(8*(z - 1))+', %r13\n')
	file_output.write('sub $'+str(z-1)+', %rdi\n')
	file_output.write('jge .L6\n')
	file_output.write('mov $'+str(i)+', %eax\n')
	file_input.close()																		
	file_output.close()															
	return 64*(z - 1)
