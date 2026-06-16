---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/landslide-detection-in-mbale-district-eastern-region-uganda-as-of-9-august-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/landslide-detection-in-mbale-district-eastern-region-uganda-as-of-9-august-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-detection-in-mbale-district-eastern-region-uganda-as-of-9-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-detection-in-mbale-district-eastern-region-uganda-as-of-9-august-2022
dataset_id: rdls_he-uga_unosat_landslidedetectionmbaledi_20220812
description: 'UNOSAT code: FL20220803UGA This map illustrates satellite-detected landslides
  in Budwale, Lwasso, Wanale, Bungokho Mutoto sub-countries and Wanale Division and
  Northern Division, Mbale district, eastern region, Uganda as observed from a Sentinel-2
  image aquired on 9 August 2022. Within the analyzed area, 27ha landslide scars are
  observed. Based on Wordlpop population data about 200,700 people live inside the
  analyzed area. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-detection-in-mbale-district-eastern-region-uganda-as-of-9-august-2022]'
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
    description: Residential population within the analyzed landslide-affected area,
      estimated at 200,700 people from WorldPop data
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
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed visual interpretation and change detection
    analysis on Sentinel-2 satellite imagery acquired on 9 August 2022 to identify
    and delineate landslide scars in Mbale district. Detected landslide features were
    digitized and attributed with area measurements. Population exposure was estimated
    by overlaying the analysis area with WorldPop gridded population data. This preliminary
    assessment has not been validated through field surveys.
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-detection-in-mbale-district-eastern-region-uganda-as-of-9-august-2022
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
  description: Landslide detection in Mbale district, eastern region, Uganda as of
    9 August 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/UG/FL20220803UGA/FL20220803UGA_gdb.zip
  format: Geodatabase
  id: resource_737912ca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220803UGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide detection in Mbale district, eastern region, Uganda as of
    9 August 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/UG/FL20220803UGA/FL20220803UGA_shp.zip
  format: null
  id: resource_b9ea636f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220803UGA_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-uga_unosat_landslidedetectionmbaledi_20220812
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-12'
temporal_resolution: null
title: Landslide detection in Mbale district, eastern region, Uganda as of 9 August
  2022
version: null
vulnerability: null
---
