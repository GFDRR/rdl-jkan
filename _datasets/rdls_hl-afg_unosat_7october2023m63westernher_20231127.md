---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da
dataset_id: rdls_hl-afg_unosat_7october2023m63westernher_20231127
description: 'UNOSAT code: EQ20231008AFG, GDACS ID: 1394952 On the 7th of October
  2023, a 6.3 magnitude earthquake struck the Herat province in the western part of
  Afghanistan. The epicentre was located 40 km north-west of Herat City and caused
  damage and destruction that triggered humanitarian needs for the local populations.
  The situation worsened when a second and a third strong earthquakes struck the region
  few days later, respectively on the 11th and 15th of October. The local government
  reported that the number of deaths was above 2000 people. After the earthquake,
  UNOSAT quickly estimated that more than a million people were living with the intensity
  zones above V. It was also estimated that between 150,000 and 230,000 buildings
  were located within the affected zones. The United Nation Office for the Coordination
  of Humanitarian Affairs (UNOCHA) reported that the worst affected districts correspond
  to Herat, Injil and Zindajan district with more than 21,500 destroyed homes. Furthermore
  in the Herat Province more than 230,000 homes have been impacted by the earthquake
  and 37,139 families have been left without home living in temporary shelter or open
  spaces (UNOCHA). At least 40 health facilities were affected during the earthquake,
  hampering the access to healthcare for an estimated of 580,000 people. One month
  after the earthquake people displaced from their home still suffer as the winter
  is approaching and temperatures are dropping (UNHCR).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da]'
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
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted post-event satellite imagery analysis by
    comparing pre- and post-earthquake satellite images to identify and map building
    damage across Herat province. Damage polygons were digitized and compiled into
    geodatabase and shapefile formats with site-level attributes including area measurements.
    The assessment captured direct physical damage from the 7 October 2023 M6.3 earthquake
    and subsequent seismic events on 11 and 15 October.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from satellite-based damage mapping
      of the October 2023 Herat earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: buildings
    asset_dimension: structure
    description: Earthquake-related fatalities reported by local government (>2000
      deaths)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
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
  description: 7 October 2023 M6.3 Western Afghanistan Herat, Preliminary Satellite-Based
    Comprehensive Damage Assessment Report (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3756/EQ20231008AFG_gdb.zip
  format: Geodatabase
  id: resource_2beea0e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 7 October 2023 M6.3 Western Afghanistan Herat, Preliminary Satellite-Based
    Comprehensive Damage Assessment Report (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3756/EQ20231008AFG_SHP.zip
  format: null
  id: resource_3d733689
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_7october2023m63westernher_20231127
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
  start: '2023-11-27'
temporal_resolution: null
title: 7 October 2023 M6.3 Western Afghanistan Herat, Preliminary Satellite-Based
  Comprehensive Damage Assessment Report
version: null
vulnerability: null
---
