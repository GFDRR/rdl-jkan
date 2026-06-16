---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016
dataset_id: rdls_hzd-sdn_unosat_geodataevolutionpossiblef_20160818
description: 'This map illustrates evolution of satellite detected waters over the
  central part of Khartoum City, Sudan, extracted from TerraSAR-X imagery (3 m) acquired
  on 11 August 2016 and SPOT-7 on 15 August 2016 (1.5 m). During this period, it has
  been observed that the water expansion is predominantly located in areas along Nile
  river banks. Additionally, the analysis carried out by UNITAR-UNOSAT also shows
  water expansion on the right bank of the Blue Nile and on the left and right banks
  of the White Nile. This analysis has not yet been validated in the field. Please
  send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016]'
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
license: CC-BY-4.0
lineage:
  description: Satellite imagery from TerraSAR-X (11 August 2016) and SPOT-7 (15 August
    2016) were analyzed by UNOSAT analysts through visual comparison to detect changes
    in water extent and saturated soil conditions. Water bodies were classified and
    mapped as vector polygons with confidence levels and area measurements. The analysis
    focused on Nile river banks and tributary areas but has not been field-validated.
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
- href: https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016
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
  description: Geodata of Evolution of Possible Flood Water & Saturated Soil Over
    Khartoum City, Khartoum State, Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN_shp.zip
  format: null
  id: resource_2d655e66
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Evolution of Possible Flood Water & Saturated Soil Over
    Khartoum City, Khartoum State, Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN.gdb.zip
  format: null
  id: resource_90eac802
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_geodataevolutionpossiblef_20160818
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-18'
temporal_resolution: null
title: Geodata of Evolution of Possible Flood Water & Saturated Soil Over Khartoum
  City, Khartoum State, Sudan
version: null
vulnerability: null
---
