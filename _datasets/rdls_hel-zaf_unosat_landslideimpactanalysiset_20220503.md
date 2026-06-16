---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kompsat-3 satellite imagery
    url: https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south
dataset_id: rdls_hel-zaf_unosat_landslideimpactanalysiset_20220503
description: 'UNOSAT code: FL20220418ZAF This map illustrates satellite-detected landslides/mudflow-related
  impact in eThekwini, Metropolitan Municipality, eThekwini District, KwaZulu-Natal
  Province, South Africa as observed from a Kompsat-3 image acquired on 21 April 2022.
  Within the analyzed area, 21 ha of landslide scars were observed. Based on Worldpop
  population data, about 55,000 people live inside the analyzed area. Within the analysis
  extent, UNITAR-UNOSAT identified 121 damaged structures and 247 potentially damaged
  structures. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south]'
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
    description: Building stock in eThekwini Metropolitan Municipality exposed to
      landslide hazard
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
    description: Residential population living within the analyzed landslide impact
      area
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
        intensity_measure: LSI:-
        process: landslide_mudflow
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed visual interpretation of Kompsat-3 satellite
    imagery acquired on 21 April 2022 to detect and delineate landslide scars and
    mudflow-affected areas in eThekwini. Damaged and potentially damaged structures
    were identified through manual feature extraction from the satellite image. Population
    exposure was estimated by overlaying the impact area with Worldpop gridded population
    data. The resulting geodatabase contains mapped hazard extents (21 ha of landslide
    scars), building damage assessments (121 confirmed and 247 potentially damaged
    structures), and population exposure estimates (~55,000 residents).
  sources:
  - id: source_1
    license: null
    name: Worldpop
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and mudflow impacts identified
      through satellite imagery analysis
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
  description: Landslide impact analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal
    Province, South Africa as of 21 April 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_gdb.zip
  format: Geodatabase
  id: resource_a8b43282
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
  description: Landslide impact analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal
    Province, South Africa as of 21 April 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_SHP.zip
  format: null
  id: resource_56ed16fc
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
slug: rdls_hel-zaf_unosat_landslideimpactanalysiset_20220503
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
  start: '2022-05-03'
temporal_resolution: null
title: Landslide impact analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal
  Province, South Africa as of 21 April 2022
version: null
vulnerability: null
---
