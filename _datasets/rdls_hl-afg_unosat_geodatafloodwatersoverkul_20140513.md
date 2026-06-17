---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kulukh-tapah-kunduz-province-afghanistan-may-13-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kulukh-tapah-kunduz-province-afghanistan-may-13-2014
dataset_id: rdls_hl-afg_unosat_geodatafloodwatersoverkul_20140513
description: 'This map illustrates satellite-detected flooded areas of Kulukh Tapah,
  Kunduz Province, Afghanistan as seen on WorldView-2 satellite imagery collected
  13 May 2014. Heavy rainfall occurred on 23-24 April 2014, causing flooding on the
  edge of town along the river bank. Approximately 27 structures have been inundated.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks, and within built-up urban areas because
  of the special characteristics of the satellite data used. This analysis has not
  yet been validated in the field. Please send ground feedback to UNITAR /UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kulukh-tapah-kunduz-province-afghanistan-may-13-2014]'
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
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared WorldView-2 satellite imagery acquired on
    13 May 2014 with reference imagery to detect changes in surface water extent following
    heavy rainfall on 23-24 April 2014. Flooded areas were manually delineated as
    polygon features, with confidence and validation flags recorded. The dataset represents
    post-event observed flood extent with noted limitations in vegetated and urban
    areas.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kulukh-tapah-kunduz-province-afghanistan-may-13-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding with approximately 27
      structures inundated
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Geodata of Flood Waters Over Kulukh Tapah, Kunduz Province, Afghanistan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG_shp.zip
  format: null
  id: resource_ee3cadfa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Kulukh Tapah, Kunduz Province, Afghanistan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG.gdb.zip
  format: null
  id: resource_456bca55
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_geodatafloodwatersoverkul_20140513
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
  start: '2014-05-13'
temporal_resolution: null
title: Geodata of Flood Waters Over Kulukh Tapah, Kunduz Province, Afghanistan
version: null
vulnerability: null
---
