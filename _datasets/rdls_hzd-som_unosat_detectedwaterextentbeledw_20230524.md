---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-beledweyne-city-beledweyne-district-hiraan-region-of-somalia-as-of-19-may-202
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-beledweyne-city-beledweyne-district-hiraan-region-of-somalia-as-of-19-may-202
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-beledweyne-city-beledweyne-district-hiraan-region-of-somalia-as-of-19-may-202
dataset_id: rdls_hzd-som_unosat_detectedwaterextentbeledw_20230524
description: "UNOSAT code FL20230327SOM, GDACS Id: 1101908 This map illustrates satellite-detected\
  \ surface waters over Beledweyne City, Beledweyne District, Hiraan Region of Somalia\
  \ as observed from a Sentinel-2 image acquired on 19 May 2023 at 07:28 UTC. Within\
  \ the analysed area of 166 km\xB2, about 63 km\xB2 of land appear to be flooded.\
  \ Water extent appears to have increased by about 9 km\xB2 since 14 May 2023. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-beledweyne-city-beledweyne-district-hiraan-region-of-somalia-as-of-19-may-202]"
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
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite image acquired on 19 May 2023 was analyzed by\
    \ UNOSAT analysts through visual interpretation and comparison with prior imagery\
    \ from 14 May 2023 to detect and delineate surface water extent. Water area was\
    \ calculated from the resulting polygon geometry (63 km\xB2 flooded area identified\
    \ within 166 km\xB2 analysis area), with change detection showing 9 km\xB2 increase\
    \ over 5 days."
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
- href: https://data.humdata.org/dataset/water-extent-beledweyne-city-beledweyne-district-hiraan-region-of-somalia-as-of-19-may-202
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extent - Beledweyne City, Beledweyne District,
    Hiraan Region of Somalia as of 19 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3598/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_4f88d963
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent - Beledweyne City, Beledweyne District,
    Hiraan Region of Somalia as of 19 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3598/FL20230327SOM_SHP.zip
  format: null
  id: resource_9471ae63
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwaterextentbeledw_20230524
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-24'
temporal_resolution: null
title: Satellite detected water extent - Beledweyne City, Beledweyne District, Hiraan
  Region of Somalia as of 19 May 2023
version: null
vulnerability: null
---
