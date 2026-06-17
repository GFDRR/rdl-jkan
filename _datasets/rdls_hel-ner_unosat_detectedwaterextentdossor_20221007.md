---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-dosso-region-niger-as-of-05-october-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-dosso-region-niger-as-of-05-october-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-dosso-region-niger-as-of-05-october-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-dosso-region-niger-as-of-05-october-2022
dataset_id: rdls_hel-ner_unosat_detectedwaterextentdossor_20221007
description: 'UNOSAT code FL20221004NER This map illustrates satellite-detected surface
  waters in Dosso Region, Niger as observed from a Sentinel-2 image acquired on 05
  October 2022 at 11:27 local time. Within the extent of this map of about 12,500
  km2, about 225 km2 of lands appear to be flooded. Based on Worldpop population data
  and the detected surface waters within the map extent, about 35,000 people are potentially
  exposed or living close to flooded areas. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-dosso-region-niger-as-of-05-october-2022]'
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
    description: Population potentially exposed or living close to flooded areas derived
      from WorldPop data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-2 satellite imagery acquired on 05 October 2022 was analyzed\
    \ by UNOSAT analysts through visual interpretation and comparison with reference\
    \ imagery to detect surface water extent. Detected flooded areas (225 km\xB2 within\
    \ 12,500 km\xB2 map extent) were intersected with WorldPop gridded population\
    \ data to estimate approximately 35,000 people potentially exposed to or living\
    \ close to flooded areas in Dosso Region, Niger."
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
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-dosso-region-niger-as-of-05-october-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas based on satellite-detected
      water extent and population distribution
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Satellite detected water extent in Dosso Region, Niger as of 05 October
    2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3396/FL20221004NER_gdb.zip
  format: Geodatabase
  id: resource_774d73b5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221004NER_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Dosso Region, Niger as of 05 October
    2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3396/FL20221004NER_SHP.zip
  format: null
  id: resource_e7698026
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221004NER_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ner_unosat_detectedwaterextentdossor_20221007
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-07'
temporal_resolution: null
title: Satellite detected water extent in Dosso Region, Niger as of 05 October 2022
version: null
vulnerability: null
---
