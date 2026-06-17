---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: University of Twente
    url: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Google Crisis Response
    url: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762
dataset_id: rdls_hzd-dma_unosat_tropicalcyclonemariainven_20170331
description: ".A large scale landslide inventory was carried out by a team from the\
  \ University of Twente, use of 5 scenes of Pl\xE9iades satellite imageries with\
  \ resolution of 0.5m, which were obtained in September 23 and October 5 after the\
  \ hurricane, made available through UNITAR-UNOSAT. Apart from these also a series\
  \ of Digital Globe Images were used that were collected for the Google Crisis Response\
  \ through a KML layer. The images were visually interpreted by image interpretation\
  \ experts, and landslides were mapped as polygons, separating scarp, transport and\
  \ accumulation areas, and classifying the landslides in types. A total of 9,960\
  \ landslides were identified, which include 8,576 debris slides, 1,010 debris flows\
  \ and 374 rock falls, with area of 7.30km2, 2.50km2, and 0.50 km2 respectively.\
  \ The whole area of landslide is 10.30 km2, which covers 1.37 percent of the island.\
  \ The source of landslides is 3.30km2, and the other 7.0 km2 is transportation and\
  \ deposition area. Almost all of the rivers flooded due to intensive precipitation.\
  \ The flooded area is 13.03km2, which covers 1.74% of the island. Dominica will\
  \ face some new problems for mountain hazards in the coming years, as many of the\
  \ fresh scarps may produce more debris, and many tree trunks are still on the slopes\
  \ or in the river channels. With so many fresh landslides in the upper catchments,\
  \ it is likely that debris flows will be triggered with rainfall thresholds that\
  \ are substantially lower than before the hurricane. Hurricane Maria damaged the\
  \ forest cover dramatically, which changed the conditions for hazard initiation.\
  \ Without the protection of vegetation, more new shallow landslides could happen\
  \ in the near future. A series of cascading hazards may happen, for example landslides\
  \ or debris flow blocking rivers and resulting in outburst floods. Therefore more\
  \ detailed evaluation of the post-Maria hazard and risk situation is very important..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_landslide_hzd
      intensity_measure: pgd:m
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: es_landslide
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  type: landslide, flood
license: CC-BY-4.0
lineage:
  description: "Post-event landslide and flood inventories were created by visual\
    \ interpretation of high-resolution satellite imagery (Pl\xE9iades 0.5m resolution\
    \ and Digital Globe imagery) acquired in September-October 2017 following Tropical\
    \ Cyclone Maria in Dominica. Image interpretation experts manually delineated\
    \ landslide polygons with morphological classification (scarp, transport, accumulation\
    \ zones) and flooded areas by comparing pre- and post-event satellite scenes."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: University of Twente
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Google Crisis Response
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762
  rel: source
loss: null
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
  description: Dominica - Tropical Cyclone Maria. Inventory of landslides and flooded
    areas (Zipped shapefile)
  download_url: https://data.humdata.org/dataset/49f301bb-20c1-4ff9-ab01-12670f234466/resource/9ff2e258-642e-40e1-bf17-80a9df41b89d/download/dominica_landslide1.zip
  format: null
  id: resource_9ff2e258
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dominica_landslide[1].zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-dma_unosat_tropicalcyclonemariainven_20170331
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
  start: '2017-03-31'
temporal_resolution: null
title: Dominica - Tropical Cyclone Maria. Inventory of landslides and flooded areas
version: null
vulnerability: null
---
