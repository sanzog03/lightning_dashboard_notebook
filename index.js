this.mbMapComparing = new mapboxgl.Map({
      attributionControl: false,
      container: this.mapContainerComparing,
      center: this.mbMap.getCenter(),
      zoom: this.mbMap.getZoom(),
      minZoom: minZoom || 4,
      maxZoom: maxZoom || 9,
      style: styleUrl,
      pitchWithRotate: false,
      dragRotate: false,
      logoPosition: 'bottom-left',
    });

let comparingId = "TRMM-LIS_FULL"
let url = "sth.com"

const tile = [`${url}VHRSC/{date}/LIS/{z}/{x}/{y}.png?colormap=terrain&stretch_range=[0.00010455249866936356,0.06766455620527267`]
// if(this.mbMapComparing.getSource(comparingId)){
    this.mbMapComparing.getSource(comparingId).tiles = tile
    // this.mbMapComparing.style.sourceCaches[comparingId].clearTiles();
    // this.mbMapComparing.style.sourceCaches[comparingId].update(this.mbMap.transform);
    // this.mbMapComparing.triggerRepaint();
// }

function baseline_link(layers, activeLayer, dateString){
    var initLink = '';
    for(var i = 0;i<layers.length;i++){
        if(layers[i].id === activeLayer){
            initLink = layers[i].source.tiles[0]
            break;
        }
    }
    initLink = initLink.replace('{date}', dateString)
    return [initLink]
}





let sth = {"source":{
                "tiles":["VHRSC/{date}/LIS/{z}/{x}/{y}.png?colormap=terrain&stretch_range=[0.00010455249866936356,0.06766455620527267]"],
                "type":"raster"
            }}