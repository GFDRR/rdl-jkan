---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsfaraf_20220215
description: 'UNOSAT code: TC20220201MDG This map illustrates satellite-detected surface
  waters in Farafangana and Vangaindrano districts, Atsimo Atsinanana region, Madagascar
  as observed from Sentinel-1 image acquired of 15 February 2022 at 05:12 local time.
  Within the analyzed area of about 1,700 km2, about 5 km2 of lands appear to be flooded.
  The water extent appears to have decreased of about 80 km2 since 8 February 2022.
  Based on Worldpop population data and the detected surface waters, about 900 people
  are potentially exposed or living close to flooded areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT. Important note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to backscattering properties of the radar signal. Satellite Data: Sentinel-1 Imagery
  Date: 15 Feb 2022 at 02:12 Local time Resolution: 10 m Copyright: Contains modified
  Copernicus Sentinel Data [2022]Source: ESA. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-]'
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery acquired on 15 February 2022 was analyzed by\
    \ UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ with imagery from 8 February 2022 to detect surface water extent changes. Detected\
    \ water polygons were intersected with WorldPop gridded population data to estimate\
    \ approximately 900 people potentially exposed to flooded areas across 5 km\xC2\
    \xB2 in the study region."
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
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by detected surface water flooding in the study
      area
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
  description: Madagascar - Satellite detected water extents in Farafangana and Vangaindrano
    districts, Atsimo Atsinanana region, as of 15 Feb.2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_gdb.zip
  format: Geodatabase
  id: resource_9b2d6391
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
  description: Madagascar - Satellite detected water extents in Farafangana and Vangaindrano
    districts, Atsimo Atsinanana region, as of 15 Feb.2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_SHP.zip
  format: null
  id: resource_48c8d4c9
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
slug: rdls_hel-mdg_unosat_detectedwaterextentsfaraf_20220215
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
  start: '2022-02-15'
temporal_resolution: null
title: Madagascar - Satellite detected water extents in Farafangana and Vangaindrano
  districts, Atsimo Atsinanana region, as of 15 Feb.2022
version: null
vulnerability: null
---
