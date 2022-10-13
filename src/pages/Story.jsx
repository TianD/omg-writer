import ReactFlow, { Controls, Background } from 'reactflow';
import 'reactflow/dist/style.css';
import TextUpdaterNode from '../nodes/TextUpdaterNode';

const nodeTypes = { textUpdater: TextUpdaterNode };

const edges = [{ id: '1-2', source: '1', target: '2' }];

const nodes = [
    {
        id: '1',
        data: { label: 'Hello' },
        position: { x: 0, y: 0 },
        type: 'textUpdater',
    },
    {
        id: '2',
        data: { label: 'World' },
        position: { x: 100, y: 100 },
    },
];

function Story() {
    return (
        <div style={{ height: '600px', width: '800px' }}>
            <ReactFlow
                nodes={nodes}
                edges={edges}
                nodeTypes={nodeTypes}
            >
                <Background />
                <Controls />
            </ReactFlow>
        </div>
    );
}

export default Story;
