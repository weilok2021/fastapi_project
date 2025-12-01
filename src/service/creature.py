import fake.creature as data
from model.creature import Creature

def get_all() -> list[Creature]:
    """Return all creatures"""
    return data.get_all()


def get_one(name: str) -> Creature | None:
    return data.get_one(name)


# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add an creature"""
    return data.create(creature)


def modify(id, creature: Creature) -> Creature:
    """Partially modify an creature"""
    return data.modify(id, creature)


def replace(id, creature: Creature) -> Creature:
    """Completely replace an creature"""
    return data.replace(id, creature)


def delete(id, creature: Creature) -> bool:
    """Delete an creature; return None if it existed"""
    return data.delete(id)