
from mido import MidiFile, tick2second; import copy; import os

file = '星茶会.mid'; mid = MidiFile(file)
tip = 0; Dict = {}; List = []; new_List = []; v = 75
name = os.path.splitext(os.path.split(file)[1])[0]

for track in mid.tracks:
    passed_time = 0
    for msg in track:
        if (msg.type == 'note_on' or msg.type == 'note_off'):
            note = [j.split('_') if j[0] == 's' else j.split('=') for j in ('state'+str(msg)[4:]).split(' ')]
            for k in range(len(note)):
                Dict[note[k][0]] = note[k][1]
            Dict['channel'] = int(Dict['channel']); Dict['time'] = int(Dict['time']) + tip
            Dict['note'] = int(Dict['note']) - 21; Dict['velocity'] = int(Dict['velocity']); tip = Dict['time']
            ab_time = tick2second(msg.time, mid.ticks_per_beat, tempo)
            real_time = ((ab_time + passed_time) * (bpm / v) * 1000 + 25) // 50; passed_time += ab_time
            if Dict['state'] == 'on':
                del Dict['state']; Dict['time'] = int(real_time); List.append(copy.deepcopy(Dict))
        else:
            try:
                tempo = msg.tempo; bpm = int(60000000/msg.tempo)
            except AttributeError:
                pass

def takeSecond(elem):
    return elem['time']

List.sort(key=takeSecond)

for k in List:
    if len(new_List) > 0 and new_List[-1]['time'] == k['time']:
        new_List[-1]['note'].append((k['channel'], k['note'], k['velocity']))
    else:
        new_List.append({'time': k['time'], 'note': [(k['channel'], k['note'], k['velocity'])]})

new_new_List = copy.deepcopy(new_List)
print(new_new_List)

for k in range(len(new_List)):
    if k != 0:
        new_new_List[k]['time'] = new_List[k]['time'] - new_List[k-1]['time']
    else:
        new_new_List[k]['time'] = 0

new_new_new_List = []; channel = ['harp']; block = ['white_stained_glass']; z = 12

for p in range(len(new_new_List)):
    new_new_new_List.append({'time': new_new_List[p]['time'], 'note': []})
    for q in new_new_List[p]['note']:
        s = int((q[2] + 12.7) // 12.8)
        for r in range(s):
            new_new_new_List[p]['note'].append((q[0], q[1]))

open('test_end.mcfunction', mode='a', encoding='utf-8').write('tp @e[tag=pos,limit=1]\n')
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('forceload add ~-16 ~-16 ~16 ~16\n')
open('test_end.mcfunction', mode='a', encoding='utf-8').write('forceload add ~-16 ~-16 ~16 ~16\n')
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('give @p minecraft:redstone_torch\n')
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('gamerule commandBlockOutput false\n')
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('summon minecraft:armor_stand ~ ~1 ~ {Tags:["pos"],Invisible:1}\n')
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z-1, 2, 14, z-1))
open('test_end.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_torch\n'.format(0, 0, -2, 0, 0, -2))
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:observer[facing=north]\n'.format(0, 0, -2, 0, 0, -2))
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:observer[facing=south]\n'.format(0, 0, -3, 0, 0, -3))
open('test_end.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:observer[facing=north]\n'.format(0, 0, -3, 0, 0, -3))
open('test_end.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:observer[facing=south]\n'.format(0, 0, -4, 0, 0, -4))
open('test_begin.mcfunction', mode='a', encoding='utf-8').write('setblock ~ ~ ~ minecraft:command_block[]{Command:"function redstone_music:test_begin_0"} destroy\n')
open('test_end.mcfunction', mode='a', encoding='utf-8').write('setblock ~ ~ ~-1 minecraft:command_block[]{Command:"function redstone_music:test_end_0"} destroy\n')

for o in range(2, z, 1):
    open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:repeater[delay=4,facing=north]\n'.format(0, 0, o, 0, 0, o))

for k in range(len(new_new_new_List)):
    open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload add ~-16 ~{} ~16 ~{}\n'.format(z-16, z+16)); i = 0
    for j in range(7):
        for x in range(-14 + 2 * j, 15 - 2 * j, 1):
            y = 2 * j
            if x == -1 or x == 1:
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:sea_lantern\n'.format(x, y, z, x, y, z))
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(x, y+1, z, x, y+1, z))
            elif x == 0:
                if y != 12:
                    open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:sea_lantern\n'.format(x, y+1, z, x, y+1, z))
                    open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(x, y+2, z, x, y+2, z))
                else:
                    open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('setblock ~{} ~-1 ~{} minecraft:command_block[facing=down]{{Command:"fill ~ ~15 ~ ~ ~15 ~ minecraft:sea_lantern"}}\n'.format(x, z))
                    open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload add ~{} ~{} ~{} ~{}\n'.format(x, z+1, x, z+1))
                    open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~14 ~{} ~{} ~14 ~{} minecraft:glass\n'.format(x, z+1, x, z+1))
                    open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload remove ~{} ~{} ~{} ~{}\n'.format(x, z+1, x, z+1))
            else:
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:diamond_block\n'.format(x, y, z, x, y, z))
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(x, y+1, z, x, y+1, z))
                if j % 2 == x % 2:
                    if i < len(new_new_new_List[k]['note']):
                        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} tutorialmod:my_note[note={},instrument={}]\n'.format(x, y, z-1, x, y, z-1, new_new_new_List[k]['note'][i][1], channel[new_new_new_List[k]['note'][i][0]]))
                        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:{}\n'.format(x, y-1, z-1, x, y-1, z-1, block[new_new_new_List[k]['note'][i][0]]))
                        i += 1  # tutorialmod:my_note
                    if i < len(new_new_new_List[k]['note']):
                        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} tutorialmod:my_note[note={},instrument={}]\n'.format(x, y, z+1, x, y, z+1, new_new_new_List[k]['note'][i][1], channel[new_new_new_List[k]['note'][i][0]]))
                        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:{}\n'.format(x, y-1, z+1, x, y-1, z+1, block[new_new_new_List[k]['note'][i][0]]))
                        i += 1  # minecraft:note_block

    if k + 2 > len(new_new_new_List):
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('forceload add ~-16 ~{} ~16 ~{}\n'.format(z-16, z+16))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z, 0, 0, z))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z, 2, 14, z))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z+1, 0, 0, z+1))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+1, 2, 14, z+1))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z+2, 0, 0, z+2))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('setblock ~{} ~{} ~{} minecraft:command_block[facing=south]{{Command:"title @p title \\"\\\\u00A7c{}\\""}}\n'.format(0, 0, z+3, name))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('setblock ~{} ~{} ~{} minecraft:chain_command_block[facing=south]{{Command:"effect clear @p",auto:1b}}\n'.format(0, 0, z+5))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('setblock ~{} ~{} ~{} minecraft:chain_command_block[facing=south]{{Command:"title @p subtitle \\"\\\\u00A7d\\\\u00a7oby-ETO\\"",auto:1b}}\n'.format(0, 0, z+4))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('setblock ~{} ~{} ~{} minecraft:chain_command_block[facing=south]{{Command:"tellraw @p {{\\"text\\":\\"Click on me to return to the dream started and reload the project -- ETO\\",\\"color\\":\\"aqua\\",\\"clickEvent\\":{{\\"action\\":\\"run_command\\",\\"value\\":\\"/function redstone_music:test_end\\"}}}}",auto:1b}}\n'.format(0, 0, z+6))
        open('test_begin.mcfunction', mode='a', encoding='utf-8').write('forceload remove ~-16 ~{} ~16 ~{}\n'.format(z-16, z+16))
    else:
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z, 0, 0, z))
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z, 2, 14, z))
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z+2, 0, 0, z+2))
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+2, 2, 14, z+2))
        if new_new_new_List[k+1]['time'] % 2 == 0:
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z, 0, 0, z))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z, 2, 14, z))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z+1, 0, 0, z+1))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+1, 2, 14, z+1))
            z -= 1
            if new_new_new_List[k+1]['time'] < 9:
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z+2, 0, 0, z+2))
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+2, 2, 14, z+2))
                z += 1
        elif new_new_new_List[k+1]['time'] % 2 == 1:
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z, 0, 0, z))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z, 2, 14, z))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_wire\n'.format(0, 0, z+1, 0, 0, z+1))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+1, 2, 14, z+1))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:sticky_piston[facing=south]\n'.format(0, 0, z+2, 0, 0, z+2))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+2, 2, 14, z+2))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:redstone_block\n'.format(0, 0, z+3, 0, 0, z+3))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+3, 2, 14, z+3))
            open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+4, 2, 14, z+4))
            z += 2
    if k + 2 <= len(new_new_new_List):
        l = new_new_new_List[k+1]['time'] // 2; n = (l + 3) // 4
        for m in range(n):
            if l >= 4:
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:repeater[delay=4,facing=north]\n'.format(0, 0, z+3+m, 0, 0, z+3+m))
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+3+m, 2, 14, z+3+m))
                l -= 4
            elif l != 0:
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:repeater[delay={},facing=north]\n'.format(0, 0, z+3+m, 0, 0, z+3+m, l))
                open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~{} ~{} ~{} ~{} ~{} ~{} minecraft:glass\n'.format(-2, 14, z+3+m, 2, 14, z+3+m))
                l = 0

    open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload remove ~-16 ~{} ~16 ~{}\n'.format(z-16, z+16))

    if k + 2 <= len(new_new_new_List):
        z += (3 + (new_new_new_List[k+1]['time'] // 2 + 3) // 4)
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('setblock ~ ~ ~ minecraft:command_block[]{{Command:"function redstone_music:test_begin_{}"}} destroy\n'.format(k+1))
        open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('setblock ~ ~ ~ minecraft:command_block[]{{Command:"function redstone_music:test_end_{}"}} destroy\n'.format(k+1))
    else:
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('effect give @p minecraft:speed 600 24 true\n')
        open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('effect give @p minecraft:speed 600 24 true\n')
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~ ~ ~ ~ ~ ~-4 minecraft:air\n')
        open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('fill ~ ~ ~ ~ ~ ~-4 minecraft:air\n')
        open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload remove ~-16 ~-16 ~16 ~16\n')
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload remove ~-16 ~-16 ~16 ~16\n')
        open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('forceload remove ~-16 ~-16 ~16 ~16\n')
        open('test_begin_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('tellraw @p {"text":"End of program operation -- ETO","color":"aqua"}\n')
        open('test_end_{}.mcfunction'.format(k), mode='a', encoding='utf-8').write('tellraw @p {"text":"End of program operation -- ETO","color":"aqua"}\n')

print(new_new_new_List)
print(bpm, ('%.2f' % (bpm/v)), len(new_new_new_List))
