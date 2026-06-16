---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/tropical-cyclone-maria-damage-density-in-the-north-western-part-of-dominica
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/tropical-cyclone-maria-damage-density-in-the-north-western-part-of-dominica
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-maria-damage-density-in-the-north-western-part-of-dominica
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-maria-damage-density-in-the-north-western-part-of-dominica
dataset_id: rdls_el-dma_unosat_tropicalcyclonemariadamag_20171003
description: 'This map illustrates potentially damaged structures and buildings in
  the north-western part of Dominica (St. John, St. Andrew, St. Peter & St. Joseph
  Parishes) as detected by satellite images acquired after landfall of the Tropical
  Cyclone Maria-17 on 19 September 2017. UNITAR-UNOSAT analysis used a Pleiades images
  acquired on 20 and 23 September 2017 as post imagery. Within the extent of this
  map UNITAR-UNOSAT identified in the cloud free zones about 3723 potentially damaged
  structures. Taking into account the pre-building footprints provided by Humanitarian
  OpenStreetMap, this represents about 70 % of the total number of structures within
  the analysed cloud free areas. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/tropical-cyclone-maria-damage-density-in-the-north-western-part-of-dominica]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building footprints in north-western Dominica identified from pre-event
      OpenStreetMap data
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-event Pleiades satellite imagery (20-23 September 2017)
    acquired after Tropical Cyclone Maria landfall on 19 September 2017. Change detection
    analysis identified 3,723 potentially damaged structures in cloud-free zones of
    north-western Dominica parishes, with results delivered as vector geodatabase
    and shapefile formats.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Pleiades satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclone-maria-damage-density-in-the-north-western-part-of-dominica
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Maria detected via post-event
      satellite imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tropical Cyclone Maria. Damage Density in the North-western Part of
    Dominica (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_gdb.zip
  format: Geodatabase
  id: resource_cee5e382
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tropical Cyclone Maria. Damage Density in the North-western Part of
    Dominica (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_shp.zip
  format: null
  id: resource_f9db043f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-dma_unosat_tropicalcyclonemariadamag_20171003
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-03'
temporal_resolution: null
title: Tropical Cyclone Maria. Damage Density in the North-western Part of Dominica
version: null
vulnerability: null
---
