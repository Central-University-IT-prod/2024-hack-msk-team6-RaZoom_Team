import { Flex, Text, Card } from "@gravity-ui/uikit";
import styles from '../../style.module.scss';
import { Editor } from "../../../../../widgets/markdownEditor/ui/editor";


const EditorLowerPart = () => {

    const onSend = (text: string) => {
        console.log(text)
    }

    return (
        <Flex direction={'column'} alignItems={'center'} justifyContent={'center'} width={'100%'} height={'100%'} gap={10}>
            <Card className={styles['card-container']} width={"75%"} view="outlined">
                <Flex centerContent spacing={{ mt: 3, mb: 6 }}>
                    <Text variant="header-2"> Редактор текста </Text>
                </Flex>
                <Flex>
                    <Editor onSubmit={onSend} />
                </Flex>
            </Card>
        </Flex>
    );
};

export default EditorLowerPart;
