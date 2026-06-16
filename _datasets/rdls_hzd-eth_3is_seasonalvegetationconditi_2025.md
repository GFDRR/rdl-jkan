---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS (Moderate Resolution Imaging Spectroradiometer)
    url: https://data.humdata.org/dataset/ethiopia-seasonal-vegetation-condition-index-june-july-august-september
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-seasonal-vegetation-condition-index-june-july-august-september
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-seasonal-vegetation-condition-index-june-july-august-september
dataset_id: rdls_hzd-eth_3is_seasonalvegetationconditi_2025
description: 'These datasets provide Ethiopia''s Vegetation Condition Index (VCI)
  values for the past five years, specifically covering the June to September growing
  season. The VCI is a satellite-derived indicator used to evaluate vegetation health
  and drought conditions. It distinguishes drought-related stress from other factors
  affecting vegetation growth. The VCI values range from 0 to 100, where 0% indicates
  the worst vegetation condition-approaching the historical minimum and signifying
  severe drought-and 100% indicates optimal conditions, near the historical maximum,
  reflecting healthy and lush vegetation. The VCI data is obtained from the MODIS
  satellite. The long-term dataset used for seasonal analysis spans from the year
  2000 to the present, focusing on the months of June through September, aligning
  with Ethiopia''s main growing season. These time series datasets enable the comparison
  of current vegetation conditions with those of recent growing seasons, supporting
  drought monitoring and vegetation health assessments.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ethiopia-seasonal-vegetation-condition-index-june-july-august-september]'
details: null
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
      intensity_measure: VCI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: MODIS satellite imagery was processed using remote sensing techniques
    to calculate the Vegetation Condition Index (VCI), a normalized indicator comparing
    current vegetation conditions to historical minimums and maximums. VCI values
    (0-100) were derived for Ethiopia's June-September growing season across five
    years (2021-2025) to identify drought-related vegetation stress independent of
    other growth factors.
  sources:
  - id: source_1
    license: null
    name: MODIS (Moderate Resolution Imaging Spectroradiometer)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-seasonal-vegetation-condition-index-june-july-august-september
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
  description: Ethiopia Seasonal Vegetation Condition Index (June, July, August, &
    September).pdf
  download_url: https://data.humdata.org/dataset/ae3e2eb9-67f3-4479-9acb-569540f04e96/resource/f2198fbb-e600-4953-8f0b-d0f2d2d1f08d/download/ethiopia-seasonal-vegetation-condition-index-june-july-august-september.pdf
  format: null
  id: resource_f2198fbb
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia Seasonal Vegetation Condition Index (June, July, August, & September).pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Seasonal Vegetation Condition Index'
  download_url: https://data.humdata.org/dataset/ae3e2eb9-67f3-4479-9acb-569540f04e96/resource/75be5a40-a613-4f6c-a69d-7817c51ee6d7/download/vci_seasonal_whole_ethiopia_2025.tif
  format: null
  id: resource_75be5a40
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VCI_Seasonal_Whole_Ethiopia_2025.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Seasonal Vegetation Condition Index'
  download_url: https://data.humdata.org/dataset/ae3e2eb9-67f3-4479-9acb-569540f04e96/resource/fa5f4c72-5dcb-44e2-862f-2755027c0585/download/vci_seasonal_whole_ethiopia_2024.tif
  format: null
  id: resource_fa5f4c72
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VCI_Seasonal_Whole_Ethiopia_2024.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Seasonal Vegetation Condition Index'
  download_url: https://data.humdata.org/dataset/ae3e2eb9-67f3-4479-9acb-569540f04e96/resource/85c6b3e4-ea17-44ff-9f60-f1f39bce0dd8/download/vci_seasonal_whole_ethiopia_2023.tif
  format: null
  id: resource_85c6b3e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VCI_Seasonal_Whole_Ethiopia_2023.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Seasonal Vegetation Condition Index'
  download_url: https://data.humdata.org/dataset/ae3e2eb9-67f3-4479-9acb-569540f04e96/resource/b7af36fe-07f1-47d4-86f6-e78f87881e8c/download/vci_seasonal_whole_ethiopia_2022.tif
  format: null
  id: resource_b7af36fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VCI_Seasonal_Whole_Ethiopia_2022.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Seasonal Vegetation Condition Index'
  download_url: https://data.humdata.org/dataset/ae3e2eb9-67f3-4479-9acb-569540f04e96/resource/41b7d0a7-24ee-4de5-b02b-4891ce9909a2/download/vci_seasonal_whole_ethiopia_2021.tif
  format: null
  id: resource_41b7d0a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VCI_Seasonal_Whole_Ethiopia_2021.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_3is_seasonalvegetationconditi_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-09-30'
  start: '2025-06-01'
temporal_resolution: null
title: 'Ethiopia: Seasonal Vegetation Condition Index'
version: null
vulnerability: null
---
