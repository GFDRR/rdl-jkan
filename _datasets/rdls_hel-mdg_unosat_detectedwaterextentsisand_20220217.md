---
attributions:
- entity:
    affiliation: null
    email: null
    name: Kompsat5 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsisand_20220217
description: 'UNOSAT code: TC20220201MDG This map illustrates satellite-detected surface
  waters in Isandra, Lalangina, and Vohibato districts, Haute Matsiatra region, Madagascar
  observed from a Kompsat5 image acquired on 12 February 2022 at 06:14 local time.
  Within the analyzed area about 1,700 km2, a total of about 10 km2 of lands appear
  to be flooded. The water extent appears to have decreased of about 40 km2 since
  8 February 2022. Based on Worldpop population data and the detected surface waters,
  about 2,400 people are potentially exposed or living close to flooded areas. This
  is a preliminary analysis that has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT). Important note: Flood
  analysis from radar images may underestimate the presence of standing waters in
  built-up areas and densely vegetated areas due to backscattering properties of the
  radar signal.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Kompsat5 satellite imagery acquired on 12\
    \ February 2022 and compared it with imagery from 8 February 2022 to detect changes\
    \ in surface water extent. Detected water polygons were intersected with WorldPop\
    \ population data to estimate exposure. The analysis covers approximately 1,700\
    \ km\xC2\xB2 in three districts of Haute Matsiatra region, Madagascar."
  sources:
  - id: source_1
    license: null
    name: Kompsat5 satellite imagery
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
- href: https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flooded areas detected from satellite imagery
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
  description: Madagascar - Satellite detected water extents in Isandra, Lalangina,
    and Vohibato districts, Haute Matsiatra region, as of 12 Feb. 22 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_gdb.zip
  format: Geodatabase
  id: resource_773465be
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220201MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Madagascar - Satellite detected water extents in Isandra, Lalangina,
    and Vohibato districts, Haute Matsiatra region, as of 12 Feb. 22 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_SHP.zip
  format: null
  id: resource_b27d3ea8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220201MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentsisand_20220217
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-02-17'
temporal_resolution: null
title: Madagascar - Satellite detected water extents in Isandra, Lalangina, and Vohibato
  districts, Haute Matsiatra region, as of 12 Feb. 22
version: null
vulnerability: null
---
