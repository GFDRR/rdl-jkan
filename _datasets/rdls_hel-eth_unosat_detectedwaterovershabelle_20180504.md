---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790
dataset_id: rdls_hel-eth_unosat_detectedwaterovershabelle_20180504
description: 'This map illustrates satellite-detected flood water extent in Somali
  Region, Ethiopia. The analysis was conducted by analysing a Sentinel-1 image acquired
  on the 1 May 2018. As observed from the satellite radar image, a total of 9,200
  ha of land were inundated in the area of interest. By using WorldPop data, we estimate
  that at least 12,000 people are potentially affected or living close to the flooded
  area. This corresponds to about 7% of the population living in the area of interest.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790]'
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
    description: Population living in or near flooded areas estimated from WorldPop
      data
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
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery from 1 May 2018 was analyzed by UNOSAT through
    visual interpretation and change detection to delineate flood water extent (9,200
    ha). Population exposure was estimated by overlaying the flood extent polygon
    with WorldPop gridded population data to quantify potentially affected residents
    in Shabelle and Afder zones, Somali Region, Ethiopia.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by or living close to flooded areas
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
  description: Satellite Detected Water Over Shabelle & Afder Zones, Ethiopia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20180501SOM/FL20180501SOM_SHP.zip
  format: null
  id: resource_c126aa02
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180501SOM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-eth_unosat_detectedwaterovershabelle_20180504
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-04'
temporal_resolution: null
title: Satellite Detected Water Over Shabelle & Afder Zones, Ethiopia
version: null
vulnerability: null
---
