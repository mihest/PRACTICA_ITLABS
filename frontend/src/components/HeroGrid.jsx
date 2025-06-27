import HeroCard from "./HeroCard.jsx";


const HeroGrid = ({members}) => {
    return (
        <div className="overflow-x-auto w-full scrollbar-hide mt-[40px] pe-[80px]">
            <div className="pl-[80px] inline-block">
                <div className="grid grid-rows-2 gap-[16px] grid-flow-col">
                    <HeroCard member={members[0]} isMain />

                    {members.slice(1).map(member => (
                        <HeroCard width={208} height={277} member={member} key={member.id} />
                    ))}
                </div>
            </div>
        </div>
    )
}
export default HeroGrid;