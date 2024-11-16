import { Flex, Card, Text } from "@gravity-ui/uikit"
import styles from '../../style.module.scss';
import DataTable from '@gravity-ui/react-data-table';


export const ProductLowerPart = () => {

    const data: DataRow[] = [
        { name: 'Алиса', role: 'Разработчик', status: 'Активен' },
        { name: 'Боб', role: 'Дизайнер', status: 'Неактивен' },
        { name: 'Чарли', role: 'Менеджер', status: 'Активен' },
    ];
    
    const columns = [
        { name: 'ИМЯ', accessor: 'name' },
        { name: 'РОЛЬ', accessor: 'role' },
        { name: 'СТАТУС', accessor: 'status' },
    ];

    
interface DataRow {
    name: string;
    role: string;
    status: string;
}
return (
    <>
    <Flex direction={'column'} alignItems={'center'} justifyContent={'center'} width={'100%'} height={'100%'} gap={10}>
            <Card className={styles['card-container']} width={"75%"} view="outlined">
                <Flex centerContent spacing={{ mt: 3, mb: 6 }}>
                    <Text variant="header-2"> Прогресс </Text>
                </Flex>
            </Card>
     {/* @ts-ignore */}
    <DataTable
        data={data}
        columns={columns}
        emptyDataMessage="Нет данных"
    />
        </Flex>
    </>
)};