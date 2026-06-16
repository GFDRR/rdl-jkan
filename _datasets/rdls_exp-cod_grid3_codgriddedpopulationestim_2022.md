---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-cod-gridded-population-estimates-v4-4
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-cod-gridded-population-estimates-v4-4
dataset_id: rdls_exp-cod_grid3_codgriddedpopulationestim_2022
description: 'Democratic Republic of the Congo gridded population estimates. This
  data release provides gridded population estimates (spatial resolution of 3 arc-seconds,
  approximately 100-metre grid cells) for the Democratic Republic of the Congo (DRC),
  along with uncertainty estimates. The data is a mosaic of gridded population estimates
  produced for all 26 provinces namely Bas-Uele, Equateur, Haut-Katanga, Haut-Lomami,
  Haut-Uele, Ituri, Kasai, Kasai-Central, Kasai-Oriental, Kinshasa, Kongo-Central,
  Kwango, Kwilu, Lomami, Lualaba, Mai-Ndombe, Maniema, Mongala, Nord-Kivu, Nord-Ubangi,
  Sankuru, Sud-Kivu, Sud-Ubangi, Tanganyika, Tshopo and Tshuapa. The project team
  used the Pre-Distribution Registration Survey (PDRS) data from the National Malaria
  Control Programme (PNLP) collected as part of anti-malarial campaigns in the DRC,
  settlement extent and geospatial covariates to model and estimate population numbers
  at grid cell level using a Bayesian statistical hierarchical modelling framework.
  Please note that PNLP data were collected across the DRC, except in Kasai, Kasai
  Central, Kasai Oriental, Kwango, Nord Ubangi and Lualaba, where the modelling utilised
  observations from neighbouring provinces The projection for all GIS files is the
  geographic coordinate system WGS84 (World Geodetic System 1984). Grid cells with
  values of NA represent areas that were mapped as unsettled according to building
  footprints data or being outside the national boundary. Suggested Dataset Citation:
  Yankey O., Nnanatu C., Boo G., Chaudhuri S., Krishnaveni K S, Megheib M, Bonnie
  A., Chamberlain H., Lazar A. N., Tatem A. J. 2025. Bottom-up gridded population
  estimates for the Democratic Republic of Congo, version 4.4. WorldPop. URL. Accessed
  DAY-MONTH-YEAR.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grid3-cod-gridded-population-estimates-v4-4]'
details: The authors followed rigorous procedures designed to ensure that the used
  data, the applied method and thus the results are appropriate and of reasonable
  quality. If users encounter apparent errors or misstatements, they should contact
  WorldPop at release@worldpop.org. WorldPop, University of Southampton, and their
  sponsors offer these data on a 'where is, as is' basis; do not offer an express
  or implied warranty of any kind; do not guarantee the quality, applicability, accuracy,
  reliability or completeness of any data provided; and shall not be liable for incidental,
  consequential, or special damages arising out of the use of any data that they offer.
  These data are operational population estimates and are not official government
  statistics.
exposure:
- asset_type:
    description: Gridded population estimates at 100-metre resolution with uncertainty
      quantification for all provinces in Democratic Republic of the Congo
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
  description: Gridded population estimates were produced by spatially disaggregating
    census and survey data to 3 arc-second (approximately 100-metre) grid cells across
    all 26 provinces of the Democratic Republic of the Congo. The dataset includes
    uncertainty estimates and represents a mosaic of provincial-level population models
    integrated into a single national grid.
  sources:
  - id: source_1
    license: null
    name: GRID3
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/grid3-cod-gridded-population-estimates-v4-4
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
  description: This geotiff raster contains the mastergrid used to define where population
    estimates were made.
  download_url: https://wopr.worldpop.org/download/614
  format: null
  id: resource_c5b8883b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v4_4_mastergrid.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DR Congo - GRID3 COD - Gridded Population Estimates v4.4 (Individual
    province dataset can be downloaded using this link.)
  download_url: https://data.worldpop.org/repo/wopr/COD/population/v4.4/Province/
  format: null
  id: resource_db9da5da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Province
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded population estimates (spatial resolution of 3 arc-seconds,
    approximately 100-metre grid cells)
  download_url: https://wopr.worldpop.org/download/613
  format: null
  id: resource_85c53324
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v4_4_gridded.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.
  download_url: https://wopr.worldpop.org/download/615
  format: null
  id: resource_12d85073
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COD_population_v4_4_README.pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cod_grid3_codgriddedpopulationestim_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: DR Congo - GRID3 COD - Gridded Population Estimates v4.4
version: null
vulnerability: null
---
