---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-mud-flow-impact-in-laurel-town-batangas-province-region-iv-a-calabarzon-philippi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-mud-flow-impact-in-laurel-town-batangas-province-region-iv-a-calabarzon-philippi
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-mud-flow-impact-in-laurel-town-batangas-province-region-iv-a-calabarzon-philippi
dataset_id: rdls_hel-phl_unosat_landslidemudflowimpactlau_20241030
description: "UNOSAT code: TC20241028PHL, GDACS ID: 1001115 This map illustrates satellite-detected\
  \ landslides in Laurel Town, Batangas Province, Region IV-A (Calabarzon), Philippines,\
  \ as observed from a Sentinel-2 image acquired on 28 October 2024 at 10:17 local\
  \ time (02:17 UTC). Within the analysed area, about 2 km\xC2\xB2 of landslide scars\
  \ /mud flow areas are observed. UNITAR-UNOSAT identified about 450 Potentially damaged\
  \ structures (6 % from the total buildings in the analysed area) and about 5 km\
  \ of affected roads. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-mud-flow-impact-in-laurel-town-batangas-province-region-iv-a-calabarzon-philippi]"
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
    description: Building stock in Laurel Town, Batangas Province, with 450 potentially
      damaged structures identified
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
- asset_type:
    description: Road network in the study area with approximately 5 km of affected
      roads
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard:
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: landslide_mudflow
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on 28
    October 2024 over Laurel Town, Batangas Province, Philippines, and identified
    landslide scars and mud flow areas through visual interpretation and comparison
    with reference imagery. Satellite-detected damage polygons were digitized and
    intersected with building footprints and road networks to quantify potentially
    affected structures and infrastructure.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-mud-flow-impact-in-laurel-town-batangas-province-region-iv-a-calabarzon-philippi
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and mud flow events in Laurel
      Town
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage to road network from landslide and mud
      flow events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Landslide/mud flow Impact in Laurel Town, Batangas Province, Region
    IV-A (Calabarzon), Philippines as of 28 Oct. 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4013/TC20241028PHL_gdb.zip
  format: Geodatabase
  id: resource_8be45a5e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241028PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide/mud flow Impact in Laurel Town, Batangas Province, Region
    IV-A (Calabarzon), Philippines as of 28 Oct. 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4013/TC20241028PHL_SHP.zip
  format: null
  id: resource_2bfd8aa3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241028PHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_landslidemudflowimpactlau_20241030
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-30'
temporal_resolution: null
title: Landslide/mud flow Impact in Laurel Town, Batangas Province, Region IV-A (Calabarzon),
  Philippines as of 28 Oct. 2024
version: null
vulnerability: null
---
