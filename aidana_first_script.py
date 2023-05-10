{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5dd3dd68",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (295393836.py, line 25)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/qd/h1rn231d183b1vyz69l8c9440000gn/T/ipykernel_10260/295393836.py\"\u001b[0;36m, line \u001b[0;32m25\u001b[0m\n\u001b[0;31m    from opentrons import simulate\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "import opentrons\n",
    "from opentrons import protocol_api\n",
    "\n",
    "metadata = {\n",
    "    'apiLevel': '2.13',\n",
    "    'protocolName': 'hewp',\n",
    "    'description': '''This protocol is me trying to see what happens if i try''',\n",
    "    'author': 'aidan'\n",
    "    }\n",
    "\n",
    "def run(protocol: protocol_api.ProtocolContext):\n",
    "    #define labware/instruments\n",
    "    wellplate96 = protocol.load_labware('conring_96_wellplate_360ul_flat', 5)\n",
    "    tips20 = protocol.load_labware('opentrons_96_tiprack_20ul', 7)\n",
    "    tips300 = protocol.load_labware('opentrons_96_tiprack_300ul', 9)\n",
    "    \n",
    "    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks='tips300')\n",
    "    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks='tips20')\n",
    "\n",
    "    #start of your protocol\n",
    "    p20.transfer(10, wellplate['A1'], wellplate['A2'], trash=False)\n",
    "    \n",
    "    if __name__ == \"__main__\":\n",
    "    # simulate this protocol\n",
    "    from opentrons import simulate\n",
    "    with open(__file__) as f:\n",
    "        logs = simulate.simulate(f, log_level=\"debug\") # for less detail: coose higher level\n",
    "    \n",
    "    # save the logs\n",
    "    cleaned_logs = [\"{}: {}\".format(log[\"payload\"][\"text\"], log[\"payload\"]) for log in logs[0]]\n",
    "    with open(\"logs.txt\", \"w+\") as f:\n",
    "        f.write(\"\\n\".join(cleaned_logs))\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eda7e944",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
