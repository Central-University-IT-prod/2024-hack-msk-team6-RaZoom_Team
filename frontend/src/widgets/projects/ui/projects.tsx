import { Card, Container, Text } from '@gravity-ui/uikit';
import { ProjectInfo } from '../../../entities/project';
import styles from './style.module.scss'
import { ProjectImg } from '../../../shared/assets';
import { Link } from 'react-router-dom';

interface Props {
    projects: ProjectInfo[]
}

export const WidgetProjectList = ({projects}: Props) => {
    return <Container>
    <div className={styles['grid-container']}>
        {projects ? projects.map(project => <Link to={'/project/'+project.id}><Card key={project.id} type='container' view='raised' className={styles['grid-item']}>
            <div className={styles['img']}>
                <img src={ProjectImg} alt="" />
            </div>
            <div style={{width: '100%'}}>
                <Text variant='header-1'>{project.name}</Text>
            </div>
        </Card>
        </Link> 
        ) : <></>}
    </div>
    </Container>
};
