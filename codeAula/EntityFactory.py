from codeAula.Background import Background
from codeAula.const import WINDOW_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i+1}', position))
                    list_bg.append(Background(f'Level1Bg{i+1}', (WINDOW_WIDTH, 0)))
                return list_bg
