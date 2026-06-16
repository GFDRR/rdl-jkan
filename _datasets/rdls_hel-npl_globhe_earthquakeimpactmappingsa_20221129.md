---
attributions:
- entity:
    affiliation: null
    email: null
    name: GLOBHE Crowddroner
    url: https://data.humdata.org/dataset/earthquake-impact-mapping-from-drones-in-sanfebagar-achham-district-nepal-november-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/earthquake-impact-mapping-from-drones-in-sanfebagar-achham-district-nepal-november-2022
creator:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/earthquake-impact-mapping-from-drones-in-sanfebagar-achham-district-nepal-november-2022
dataset_id: rdls_hel-npl_globhe_earthquakeimpactmappingsa_20221129
description: 'Earthquake impacts mapping from drone data in Nepal (Sanfebagar, Achham
  District, Sudurpashchim Province) from GLOBHE Crowddroner. The dataset includes
  high-resolution actionable drone data showing the area impacted from the earthquakes
  of early November 2022. Reference: https://reliefweb.int/disaster/eq-2022-000358-npl
  MORE CROWDDRONING BY GLOBHE Web: https://globhe.com/ Facebook: https://www.facebook.com/Crowddroning
  Twitter: https://twitter.com/globhedrones Instagram: https://www.instagram.com/globhedrones/
  LinkedIn: https://www.linkedin.com/company/globhedrones/. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/earthquake-impact-mapping-from-drones-in-sanfebagar-achham-district-nepal-november-2022]'
details: null
exposure:
- asset_type:
    description: Building stock visible in drone orthomosaic and panoramic imagery
      in the impacted area
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Drone survey data collected by GLOBHE Crowddroner in November 2022
    following the early November 2022 earthquake in Achham District, Nepal. High-resolution
    orthomosaic and panoramic imagery were processed to document earthquake impacts
    on buildings and infrastructure in Sanfebagar. The dataset provides direct observational
    evidence of ground motion damage effects.
  sources:
  - id: source_1
    license: null
    name: GLOBHE Crowddroner
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/earthquake-impact-mapping-from-drones-in-sanfebagar-achham-district-nepal-november-2022
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from November 2022 earthquake ground motion
      observed in drone survey
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Earthquake impact mapping from drones in Sanfebagar, Achham District,
    Nepal (November 2022) (High-resolution 360 panorama from GLOBHE Crowddroner in
    Sanfebagar, Nepal.)
  download_url: https://data.humdata.org/dataset/15375f57-9a9a-4449-95aa-5e8a76ba3c11/resource/1f80ee51-7355-49d7-ab68-fa1c0327f866/download/dji_0015.jpg
  format: JPEG
  id: resource_1f80ee51
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sanfebagar_Nepal_360_Panorama_4_GLOBHE.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Earthquake impact mapping from drones in Sanfebagar, Achham District,
    Nepal (November 2022) (High-resolution 360 panorama from GLOBHE Crowddroner in
    Sanfebagar, Nepal.)
  download_url: https://data.humdata.org/dataset/15375f57-9a9a-4449-95aa-5e8a76ba3c11/resource/9b83079f-dfed-45ab-9dd4-2af7e85519c2/download/dji_0014.jpg
  format: JPEG
  id: resource_9b83079f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sanfebagar_Nepal_360_Panorama_3_GLOBHE.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Earthquake impact mapping from drones in Sanfebagar, Achham District,
    Nepal (November 2022) (High-resolution 360 panorama from GLOBHE Crowddroner in
    Sanfebagar, Nepal.)
  download_url: https://data.humdata.org/dataset/15375f57-9a9a-4449-95aa-5e8a76ba3c11/resource/403f6ff6-dc61-46f8-a456-87e1d2eacf41/download/dji_0013.jpg
  format: JPEG
  id: resource_403f6ff6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sanfebagar_Nepal_360_Panorama_2_GLOBHE.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Earthquake impact mapping from drones in Sanfebagar, Achham District,
    Nepal (November 2022) (High-resolution 360 panorama from GLOBHE Crowddroner in
    Sanfebagar, Nepal.)
  download_url: https://data.humdata.org/dataset/15375f57-9a9a-4449-95aa-5e8a76ba3c11/resource/f12fda9b-d05b-48ef-8517-14f962cdaf4d/download/dji_0012.jpg
  format: JPEG
  id: resource_f12fda9b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sanfebagar_Nepal_360_Panorama_1_GLOBHE.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'High-resolution orthomosaic, showing the area impacted from the earthquake
    happened on early November 2022. Area: 24.3 hectares Spatial resolution: 2.9 cm/px'
  download_url: https://data.humdata.org/dataset/15375f57-9a9a-4449-95aa-5e8a76ba3c11/resource/42ae1045-5aa4-4010-b0d1-fa9bf530bca8/download/kalimati_orthomosaic.tif
  format: null
  id: resource_42ae1045
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sanfebagar_Nepal_Orthomosaic_GLOBHE.tif
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_globhe_earthquakeimpactmappingsa_20221129
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-29'
temporal_resolution: null
title: Earthquake impact mapping from drones in Sanfebagar, Achham District, Nepal
  (November 2022)
version: null
vulnerability: null
---
