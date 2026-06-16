---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/sweden-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/sweden-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/sweden-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-swe_metad4g_highresolutionpopulationd_20210713
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Sweden: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/sweden-high-resolution-population-density-maps-demographic-estimates]'
details: "Citation To reference this data, please use the following citation: Meta\
  \ and Center for International Earth Science Information Network - CIESIN - Columbia\
  \ University. 2021. High Resolution Settlement Layer (HRSL). Source imagery for\
  \ HRSL \xC2\xA9 2021 Maxar. Accessed DAY MONTH YEAR. Acknowledgements CIESIN contributions\
  \ to the development of this work were supported by funding provided by Meta. Population\
  \ estimates are based on data from the Gridded Population of the World data collection.\
  \ Imagery used to identify settlements is from the Maxar Basemap +Vivid. Data for\
  \ the surface model relies on digital surface model produced with the data from\
  \ the Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM) on board\
  \ the Advanced Land Observing Satellite (ALOS); additional house locations come\
  \ from OpenStreetMap Please note that as of 2024, Meta's high resolution population\
  \ density maps are no longer being updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Sweden disaggregated
      by demographic groups (overall, women, men, children 0-5, youth 15-24, elderly
      60+, women of reproductive age 15-49)
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify buildings from commercial satellite imagery, then
    overlaying general population estimates derived from Swedish census data and other
    public population statistics in collaboration with Columbia University. The resulting
    gridded datasets provide demographic disaggregation at fine spatial resolution
    for disaster risk exposure assessment.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
    risk_data_type:
    - exposure
    type: dataset
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
- href: https://data.humdata.org/dataset/sweden-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/89be8216-5506-48ff-9687-241080b95b85/download/swe_general_2020_csv.zip
  format: null
  id: resource_89be8216
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/9b6f7654-6f98-4a63-9738-dfcb8f464654/download/swe_general_2020_geotiff.zip
  format: null
  id: resource_9b6f7654
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/c12c0656-32ee-415f-90a7-75dfa714cdca/download/swe_children_under_five_2020_csv.zip
  format: null
  id: resource_c12c0656
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/39225ba2-45af-4087-b790-4b266f6756ae/download/swe_children_under_five_2020_geotiff.zip
  format: null
  id: resource_39225ba2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/33b7ff36-d58e-40ef-bb93-7d4faeceeccc/download/swe_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_33b7ff36
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/c892b060-ccbf-4ec4-8e1e-b63ce8bede2c/download/swe_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_c892b060
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/4e3462d4-0206-4a86-8e1c-0b7f74404856/download/swe_men_2020_csv.zip
  format: null
  id: resource_4e3462d4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/44f9a1db-9eb4-4598-a868-fa8dac4ee156/download/swe_men_2020_geotiff.zip
  format: null
  id: resource_44f9a1db
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/e9a63916-1283-4a44-b26b-8d314deac1e1/download/swe_women_2020_csv.zip
  format: null
  id: resource_e9a63916
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/fa99dd29-2760-4195-a38f-3015d8cdc5d3/download/swe_women_2020_geotiff.zip
  format: null
  id: resource_fa99dd29
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/17aa0b41-235c-4cf9-b4f1-084555309262/download/swe_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_17aa0b41
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/baa9a444-bcbd-4306-854a-cc324574f79b/download/swe_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_baa9a444
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/13148481-62d2-4455-820c-f3f36fabbbc5/download/swe_youth_15_24_2020_csv.zip
  format: null
  id: resource_13148481
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sweden: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bdb28c9c-3f48-4740-b6bd-952b2dcf2574/resource/c22c92b9-33d0-4edd-8dba-47c4c7b40017/download/swe_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_c22c92b9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-swe_metad4g_highresolutionpopulationd_20210713
spatial:
  bbox: null
  centroid: null
  countries:
  - SWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-13'
temporal_resolution: null
title: 'Sweden: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
