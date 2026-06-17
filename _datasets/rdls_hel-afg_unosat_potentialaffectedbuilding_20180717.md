---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-affected-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-affected-
dataset_id: rdls_hel-afg_unosat_potentialaffectedbuilding_20180717
description: 'This map illustrates satellite-detected landslide and flood water extent
  in Peshghor village and surrounding areas in Khenj District, Panjshir Province,
  Afghanistan as seen on Sentinel-2 satellite imagery, 10 m resolution, collected
  on 13 July 2018, one day after the disaster happened. The landslides and floodwaters
  hit villages downstream because of the break-up of the natural banks of the dam.
  As a result, Peshghor and surrounding villages have been cut off and damages have
  been reported on structures and buildings. Within the current map extent Saricha
  primary road is potentially affected by the landslides and the overflow of Panjshir
  River. Around 198 buildings are located within areas affected by the landslide and
  9 within areas affected by the floods. Due to the resolution of the satellite imagery,
  the extent of landslide and floodwaters may be underestimated and as a consequence,
  the number of buildings potentially affected. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potential-affected-]'
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
    description: Building structures potentially affected by landslide and flood hazards
      in Peshghor village
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
    description: Saricha primary road potentially affected by landslide and flood
      hazards
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared Sentinel-2 satellite imagery from 13 July
    2018 (one day post-disaster) with reference imagery to detect and delineate landslide
    and flood water extents in Peshghor village, Khenj District, Afghanistan. The
    analysis identified hazard footprints and overlaid them with building and infrastructure
    features to assess potential impacts from the natural dam breach event.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/potential-affected-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide in Peshghor village
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding in Peshghor village
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  description: Potential affected buildings & impact caused by landslide and floods
    in Peshghor village in Khenj District, Afghanistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/LS20180712AFG/LS20180712AFG_SHP.zip
  format: null
  id: resource_ad687285
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20180712AFG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-afg_unosat_potentialaffectedbuilding_20180717
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-17'
temporal_resolution: null
title: Potential affected buildings & impact caused by landslide and floods in Peshghor
  village in Khenj District, Afghanistan
version: null
vulnerability: null
---
