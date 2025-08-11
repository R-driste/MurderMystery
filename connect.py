import badge

class App(badge.BaseApp):
    def on_open(self) -> None:
        self.all_active_contacts = []
        self.assignments = []
        self.host_id = 888

    def send_badge_id_to_host(self):
        my_contact = badge.contacts.my_contact()
        badge_id = None
        if my_contact is not None:
            badge_id = getattr(my_contact, "badge_id", None)
        if badge_id is None:
            badge_id = badge.info.badge_id()
        packet = badge_id.to_bytes(4, 'big')
        badge.radio.send_packet(self.host_id, packet)
        self.logger.info(f"Successfully sent badge ID {badge_id} to host {self.host_id}.")

    def on_packet(self, packet: bytes, in_foreground: bool) -> None:
        if len(packet) >= 4:
            sender_badge_id = int.from_bytes(packet[0:4], "big")
            contact = badge.contacts.get_contact_by_badge_id(sender_badge_id)
            self.logger.info(f"Received badge ID and contact: {sender_badge_id}")
            self.all_contacts.append(contact)
        else:
            self.logger.warning("Received malformed packet")

    def assign_killers(self) -> None:
        if len(self.all_contacts) < 2:
            self.logger.warning("Not enough contacts to assign killers!")
            return
        else:
            needed_nums = self.get_pseudo_random()
            self.assignments = needed_nums
    
    def get_pseudo_random():
        valid = False
        while not valid:
            num_len = len(self.all_active_contacts)
            input_str = f"{num_len}_{badge.time.monotonic()}"
            hash_pos_val = str(abs(hash(input_str)))
            input_str_2 = f"{badge.time.monotonic()}_{num_len}"
            hash_pos_val += str(abs(hash(input_str_2)))

            fix = ""
            i = 1
            unique = ['0']
            print(hash_pos_val)
            for char in hash_pos_val:
                print(char, ",", unique, ",", fix)
                c = int(char)
                if c > num_len or c == i or str(c) in unique:
                    continue
                else:
                    i += 1
                    fix += char
                    unique.append(char)

            print(fix)
            valid = True if len(fix) == num_len else False
        return fix

"""
class Contact():
    def __init__(self, name: str):
        self.name = name
        self.pronouns = "unassigned"
        self.badge_id = True
        self.handle = 0
"""