import { LikeOutlined, MessageOutlined, StarOutlined } from '@ant-design/icons';
import { Avatar, List, Space } from 'antd';
import { Link } from 'react-router-dom';
import React from 'react'

const data = Array.from({
    length: 23,
}).map((_, i) => ({
    title: <Link to={`story/${i}`} >{`ant design part ${i}`}</Link>,
    avatar: 'https://joeschmoe.io/api/v1/random',
    description:
        'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content:
        'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
}));

const IconText = ({ icon, text }) => (
    <Space>
        {React.createElement(icon)}
        {text}
    </Space>
);

const Home = () => (
    <List
        itemLayout="vertical"
        size="large"
        pagination={false}
        dataSource={data}
        footer={
            <div>
                <b>ant design</b> footer part
            </div>
        }
        renderItem={(item) => (
            <List.Item
                key={item.title}
                actions={[
                    <IconText icon={StarOutlined} text="156" key="list-vertical-star-o" />,
                    <IconText icon={LikeOutlined} text="156" key="list-vertical-like-o" />,
                    <IconText icon={MessageOutlined} text="2" key="list-vertical-message" />,
                ]}
                extra={
                    <img
                        width={272}
                        alt="logo"
                        src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                    />
                }
            >
                <List.Item.Meta
                    avatar={<Avatar src={item.avatar} />}
                    title={item.title}
                    description={item.description}
                />
                {item.content}
            </List.Item>
        )}
    />
);

export default Home;