---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kompsat-3 satellite imagery
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr
dataset_id: rdls_hel-zaf_unosat_landslideimpactanalysiset_20220506
description: 'UNOSAT code: FL20220418ZAF This map illustrates satellite-detected landslides/mudflow
  in eThekwini, Metropolitan Municipality, eThekwini District, KwaZulu-Natal Province,
  South Africa as observed from a Kompsat-3 image acquired on 21 April 2022. Within
  the analyzed area, 270 ha of landslide scars were observed. Based on Worldpop population
  data, about 283,000 people live inside the analyzed area. Within the analysis extent,
  UNITAR-UNOSAT identified 506 damaged structures and 197 potentially damaged structures.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr]'
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
    description: Building structures identified in the landslide impact area
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
    description: Residential population living within the analyzed landslide extent
      based on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts interpreted Kompsat-3 satellite imagery acquired on
    21 April 2022 to detect and delineate landslide scars and mudflow features in
    eThekwini. Damaged and potentially damaged structures were identified through
    visual analysis of satellite imagery. Population exposure was estimated by overlaying
    the impact area with WorldPop gridded population data. The resulting geodatabase
    contains mapped landslide extents (270 ha), structure damage assessments (506
    confirmed, 197 potential), and population estimates (283,000 residents).
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Kompsat-3 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and mudflow impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
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
  description: Landslide impact analysis in eThekwini, Metropolitan Municipality,
    South Africa as of 21 April 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_gdb.zip
  format: Geodatabase
  id: resource_1ad03dc5
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
  description: Landslide impact analysis in eThekwini, Metropolitan Municipality,
    South Africa as of 21 April 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_SHP.zip
  format: null
  id: resource_3afca141
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
- loss
schema: rdls-10
slug: rdls_hel-zaf_unosat_landslideimpactanalysiset_20220506
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
  start: '2022-05-06'
temporal_resolution: null
title: Landslide impact analysis in eThekwini, Metropolitan Municipality, South Africa
  as of 21 April 2022
version: null
vulnerability: null
---
