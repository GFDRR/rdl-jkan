---
attributions:
- entity:
    affiliation: null
    email: null
    name: AI and Data for Good at Meta (Facebook)
    url: https://data.humdata.org/dataset/saint-kitts-and-nevis-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/saint-kitts-and-nevis-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/saint-kitts-and-nevis-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/saint-kitts-and-nevis-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-kna_metad4g_saintkittsnevishighresolu_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Saint Kitts and Nevis: (1) Overall
  population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24)
  (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/saint-kitts-and-nevis-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.'"
exposure:
- asset_type:
    description: Overall high-resolution population density estimates for Saint Kitts
      and Nevis derived from satellite imagery and census data
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints are extracted from commercial satellite imagery
    using machine learning techniques developed by Meta. These footprints are then
    combined with national census data and ancillary population statistics in partnership
    with Columbia University to disaggregate population counts to high-resolution
    grid cells. The resulting raster and CSV datasets provide spatially explicit demographic
    estimates for use in disaster risk exposure assessments.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta (Facebook)
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Columbia University
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/saint-kitts-and-nevis-high-resolution-population-density-maps-demographic-estimates
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/methodology-high-resolution-population-density-maps-demographic-estimates/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/high-resolution-population-density-maps-demographic-estimates-documentation/
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/census-information-for-high-resolution-population-density-maps/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/69313751-399a-4583-b344-6c6ffcc911ec/download/population_kna_2018-10-01.csv.zip
  format: null
  id: resource_69313751
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_kna_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/e7b1c188-99e8-4b6d-99b7-c33c8d2c377f/download/population_kna_2018-10-01.zip
  format: null
  id: resource_e7b1c188
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_kna_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/f71137fa-6f61-47de-bb50-2c9622c02c26/download/kna_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_f71137fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/e15ae20f-cc82-4d9e-8469-8f419e733120/download/kna_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_e15ae20f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/bfea3a44-cd4a-4994-8b96-4d1ecb31e006/download/kna_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_bfea3a44
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/776bf973-72e9-478f-8250-edfafd635fe6/download/kna_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_776bf973
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/b85bdc95-a320-4a88-86de-47ec5110c00d/download/kna_men_2019-06-01_csv.zip
  format: null
  id: resource_b85bdc95
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/73f19fab-f0e6-46fc-b80a-b11acdb6eec5/download/kna_men_2019-06-01_geotiff.zip
  format: null
  id: resource_73f19fab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/55175541-e7eb-4162-b2d4-a05ae174bf27/download/kna_women_2019-06-01_csv.zip
  format: null
  id: resource_55175541
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/749083d3-e437-4b0c-af44-08249f0dd597/download/kna_women_2019-06-01_geotiff.zip
  format: null
  id: resource_749083d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/78c3f0ab-ed70-4e54-bd55-40aaea3cdca1/download/kna_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_78c3f0ab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/2aeaf1da-e151-4f3a-9a99-ca657b526103/download/kna_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_2aeaf1da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/a1d181ce-96df-404c-9cb4-a267a54d1b9b/download/kna_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_a1d181ce
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0645fa18-489a-4516-8221-91f5c134935b/resource/07d8870a-34a3-4891-8ad5-1de4136c55a3/download/kna_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_07d8870a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KNA_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-kna_metad4g_saintkittsnevishighresolu_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - KNA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'Saint Kitts and Nevis: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
