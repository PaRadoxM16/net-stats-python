stats_location = "/sys/class/net/[]/statistics/"

def net_stats(interface):
    file_location = stats_location.replace("[]", interface)
    all_stats = {
        'rx_packets': None,
        'tx_packets': None,
        'rx_bytes': None,
        'tx_bytes': None
    }
    for stat in all_stats:
        with open(file_location+stat) as file:
            value = int(file.read().strip())
            all_stats[stat] = value

    return all_stats

print(net_stats('eth0'))
