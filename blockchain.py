from genesis_block import genesis_block
from new_block import new_block
import time as tm

blockchain = [genesis_block()]
block_genesis = blockchain[0] 

print("\nBlock #{} added to the blockchain!".format(block_genesis.index))
print("Timestamp: {}".format(block_genesis.timestamp))
print("Data: {}".format(block_genesis.data))
print("Previous Hash: {}".format(block_genesis.previous_hash))
print("Hash: {}\n".format(block_genesis.hash))
tm.sleep(3)

numOfBlocks = 10
previous_block = block_genesis
for i in range(0,numOfBlocks):
	current_block = new_block(previous_block)
	blockchain.append(current_block)
	previous_block = current_block

	print("Block #{} added to the blockchain!".format(current_block.index))
	print("Timestamp: {}".format(current_block.timestamp))
	print("Data: {}".format(current_block.data))
	print("Previous Hash: {}".format(current_block.previous_hash))
	print("Hash: {}\n".format(current_block.hash))

	tm.sleep(3)
