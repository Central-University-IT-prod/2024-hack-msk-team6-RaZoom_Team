import { NotFound } from '@gravity-ui/illustrations';
import { Button, Flex } from '@gravity-ui/uikit';
import { Link } from 'react-router-dom';
// import { Link } from 'react-router-dom';

const NotFoundPage = () => {
    return (
        <Flex direction={"column"} alignItems={"center"} justifyContent={"center"}>
            <NotFound />
            <Link to={"/"}>
            {/* @ts-ignore */}  
                <Button  size="l" width="max" view="action">На главную</Button>
            </Link>
        </Flex>


    );
};

export default NotFoundPage;
