---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-as-of-13-may-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-as-of-13-may-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-as-of-13-may-2020
dataset_id: rdls_hel-som_unosat_detectedwateridpdistribut_20200514
description: 'UNOSAT code: FL20200428SOM This map illustrates the flood-affected sectors
  of Beletweyne town in Hiiran Region, Somalia as detected from the analysis of a
  satellite Worldview-2 images acquired on the 13 May 2020. Belet Weyne is heavily
  affected by floods and about 50% of the town and its vicinity is largely inundated;
  the sectors called Kutimbo, Radar, and Lamagalay Regional Military Base appear to
  be the most affected by floodwaters as of 13 May 2020. More than 110 IDP sites are
  located inside of the town and 25% of them are located within the completely flooded
  areas. This is a preliminary analysis and has not been validated in the field yet.
  Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-as-of-13-may-2020]'
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
    description: Building structures affected by flood inundation in Beletweyne town
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
      quantity_kind: area
      unit: null
- asset_type:
    description: IDP populations located in camps within and outside flood-affected
      areas
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
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts analyzed Worldview-2 satellite imagery acquired on
    13 May 2020 over Beletweyne town, Somalia, comparing multi-temporal images to
    detect flood-affected sectors and inundation extent. Spatial data on flooded areas
    and IDP camp locations were extracted and vectorized into geodatabase and shapefile
    formats to document the 50% inundation of the town and the 25% of IDP sites located
    within completely flooded areas.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-as-of-13-may-2020
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building inundation and damage from fluvial flooding in Beletweyne
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
  - asset_category: population
    asset_dimension: population
    description: IDP populations affected by flood inundation in camps
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
  description: Somalia - Satellite detected water & IDP distribution over Belet Weyne
    Town (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20200428SOM/FL20200428SOM_gdb.zip
  format: Geodatabase
  id: resource_ebecb888
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200428SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Satellite detected water & IDP distribution over Belet Weyne
    Town (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20200428SOM/FL20200428SOM_SHP.zip
  format: null
  id: resource_c2a6b3a5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200428SOM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_unosat_detectedwateridpdistribut_20200514
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-05-14'
temporal_resolution: null
title: Somalia - Satellite detected water & IDP distribution over Belet Weyne Town
version: null
vulnerability: null
---
