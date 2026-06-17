---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa
dataset_id: rdls_he-zaf_unosat_landslideanalysisethekwin_20220429
description: 'UNOSAT code: FL20220418ZAF This map illustrates satellite-detected landslides/mudflow
  in eThekwini, Metropolitan Municipality, eThekwini District, KwaZulu-Natal Province,
  South Africa as observed from a Sentinel-2 image acquired on 28 April 2022.Within
  the analyzed area, 11 ha of landslide scars were observed. Based on Worldpop population
  data, about 27,000 people live inside the analyzed area. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa]'
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
    description: Residential population within the analyzed landslide-affected area
      based on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts visually interpreted Sentinel-2 satellite imagery acquired
    on 28 April 2022 to detect and delineate landslide scars and mudflow features
    in eThekwini. Detected hazard polygons were attributed with area measurements.
    Population exposure was estimated by intersecting the hazard area with WorldPop
    gridded population data. This is a preliminary post-event satellite-based damage
    assessment not yet validated in the field.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa
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
  description: Landslide analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal
    Province, South Africa as of 28 April 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_gdb.zip
  format: Geodatabase
  id: resource_1da0b980
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220418ZAF_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal
    Province, South Africa as of 28 April 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_SHP.zip
  format: null
  id: resource_67234350
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220418ZAF_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-zaf_unosat_landslideanalysisethekwin_20220429
spatial:
  bbox: null
  centroid: null
  countries:
  - ZAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-04-29'
temporal_resolution: null
title: Landslide analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal Province,
  South Africa as of 28 April 2022
version: null
vulnerability: null
---
