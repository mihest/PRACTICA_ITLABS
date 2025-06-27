


const HeroCard = ({member, isMain}) => {
    const image = member.image ? member.image : '/zagl.png';
    const full_name = member.name?.trim().split(/\s+/) ?? [];
    return (
        <div
            className={`relative bg-cover bg-center ${isMain ? 'w-[428px] h-[571px] row-span-2' : 'w-[208px] h-[277px]'}`}
            style={{ backgroundImage: `url(${image})` }}
        >
            {/* Цветовой фильтр поверх картинки */}
            <div className="absolute inset-0 bg-[#fae4c2]/90 mix-blend-multiply pointer-events-none" />
            <div className={`absolute bottom-0 left-0 w-full ${isMain ? 'h-[247px]' : 'h-[120px]'} bg-gradient-to-t from-[#262421] to-transparent pointer-events-none z-10} />`} />
            <span className={`text-white absolute bottom-[4%] left-[5%] ${isMain ? 'text-[28px]/[32px] font-[700]' : 'text-[16px]/[18px] font-[700]'}`}>{full_name[0] + ' ' + full_name[1]}<br/>{full_name[2] && full_name[2]}</span>
        </div>
    )
}
export default HeroCard;