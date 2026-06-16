---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/satellite-detected-water-over-dadaab-sub-county-garissa-county-2802
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-dadaab-sub-county-garissa-county-2802
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-dadaab-sub-county-garissa-county-2802
dataset_id: rdls_hl-ken_unosat_detectedwateroverdadaabsu_20180515
description: 'This map illustrates satellite-detected flood water extent over Dadaab
  & Lagdera Sub Counties, Garissa County, Kenya. The analysis was conducted analyzing
  Sentinel-1 image acquired on the 4 May 2018. Within the analysis extent, ~ 43,300
  ha of land appear to be inundated and around 23,000 people are living inside this
  flood water extent. Within the analysis extent, around 23,300 ha of inundated land
  are located inside Dabaad Sub County, potentially affecting 18,200 people. Several
  refugee camps, specially the ones located inside Dadaab Sub County, seem to be affected
  by the floods, being Ifo 2 Refugee Camp the most affected one. It is likely that
  flood waters have been systematically underestimated along highly vegetated areas
  along main river banks and within built-up urban areas because of the special characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-dadaab-sub-county-garissa-county-2802]'
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
  - analysis_type: deterministic
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
  description: Sentinel-1 SAR imagery acquired on 4 May 2018 was analyzed by UNOSAT
    using satellite image comparison and change detection techniques to map inundated
    land areas. The resulting flood extent polygons (area_ha, area_m2) were intersected
    with population data to estimate the number of people potentially affected within
    Dadaab and Lagdera Sub Counties, Garissa County, Kenya.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-over-dadaab-sub-county-garissa-county-2802
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people living within the satellite-detected flood
      water extent in Dadaab and Lagdera Sub Counties
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Kenya - Satellite detected water over Dadaab Sub County, Garissa County
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/KE/FL20180508KEN/FL20180508KEN_shp.zip
  format: null
  id: resource_d5a79ab9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180508KEN_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-ken_unosat_detectedwateroverdadaabsu_20180515
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-15'
temporal_resolution: null
title: Kenya - Satellite detected water over Dadaab Sub County, Garissa County
version: null
vulnerability: null
---
