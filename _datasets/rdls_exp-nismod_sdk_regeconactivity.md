---
catalog: null
contact_point:
  email: tom.russell@ouce.ox.ac.uk
  id: attribution_contact
  name: Tom Russell
  url: https://www.eci.ox.ac.uk/person/tom-russell
creator:
  email: tom.russell@ouce.ox.ac.uk
  id: attribution_creator1
  name: Tom Russell
  url: https://www.eci.ox.ac.uk/person/tom-russell
dataset_id: rdls_exp-nismod_sdk_regeconactivity
description: 'A curated collection of open geospatial datasets processed to support
  downscaling of regional economic activity from national/subnational levels to high-resolution
  grids globally. The collection includes agricultural GDP by subsector (crop, livestock,
  forestry, fisheries), gridded GDP data, built environment indicators, points of
  interest from Overture Maps and Foursquare, population and settlement layers, land
  cover classifications, power generation facilities, and mining locations. All datasets
  are harmonized to cloud-optimized Parquet format and H3 hexagonal grid system to
  enable analysis of economic activity distribution across three dimensions: Location
  (high spatial resolution), Category (economic sectors following ISIC classification),
  and Output (GDP/GVA quantification). This package provides standardized inputs for
  developing Bayesian Hierarchical Models that infer 20-sector gridded regional Gross
  Value Added (rGVA) globally by incorporating multi-scale, multi-sector priors.'
details: 'This is version 0.1.0 of a curated data package developed for the validation
  workshop - Downscaling of global economic activity data - held at Oxford University
  on 15 May 2025. All datasets have been transformed from their original sources into
  cloud-optimized Parquet format and spatially harmonized using H3 hexagonal grid
  (resolutions 7-10, approximately 5km-100m cell sizes) via the scalenav framework
  built on DuckDB and Ibis for large-scale spatial analysis. The processing methodology
  implements pycnophylactic spatial downscaling (mass-preserving interpolation) and
  maps Points of Interest to ISIC codes for sector-specific economic disaggregation.
  Datasets are accessible via cloud object storage (S3: s3://gri-datapkg/spatial-economics/v0.1.0/)
  without download requirements. All data sources are attributed to original creators
  and carry their respective licenses; processing code is available under MIT license
  on GitHub. Spatial coverage is global with example applications in UK, Thailand,
  and Ghana; temporal coverage spans primarily 2010-2024 with some historical data
  to 1990. The final model outputs (20-sector gridded rGVA globally) are work-in-progress
  and will be released separately; this package contains input and validation datasets
  used in model development.'
exposure:
  category: buildings, economic_indicator, infrastructure, natural_environment, population
  dimension: content, population, product, structure
  quantity_kind: area, count, monetary, power
  taxonomy: GED4ALL
extra_attributions:
- email: fcdo.correspondence@fcdo.gov.uk
  id: attribution_funder
  name: UK Foreign, Commonwealth and Development Office (FCDO)
  role: funder
  url: https://www.gov.uk/government/organisations/foreign-commonwealth-development-office
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Climate Compatible Growth (CCG)
  url: https://climatecompatiblegrowth.com/
publisher:
  email: info@zenodo.org
  id: attribution_publisher
  name: Zenodo
  url: https://zenodo.org
purpose: Provides standardized, analysis-ready geospatial datasets to support research
  on spatial economic modeling, infrastructure-economy interactions, and climate risk
  assessment. Addresses the critical gap in understanding how economic activity distributes
  spatially by enabling researchers to downscale coarse national/regional economic
  statistics to high-resolution grids while maintaining sectoral detail. Facilitates
  data-driven analysis of economic exposure in infrastructure climate risk assessments,
  regional economic planning, and sustainable development research. The processed
  datasets eliminate barriers to access by providing harmonized formats optimized
  for large-scale spatial analysis and machine learning applications in economic geography.
resources:
- coordinate_system: null
  description: 'JSON file mapping dataset identifiers to their S3 cloud storage paths
    for direct access. Contains 18 entries pointing to processed Parquet datasets
    including: agricultural GDP subsectors (crop, fish, forest, livestock, total),
    Copernicus built-up area, DOSE-WDI economic output, GEM power tracker, JRC population
    and settlement layers (aggregated, building height, population, settlement area
    for 2018 and non-residential), Kummu GDP PPP, MAPSPAM crop yields, mining locations,
    and Overture places with land use (both filled and original versions). All datasets
    stored in cloud-optimized Parquet format at s3://gri-datapkg/spatial-economics/v0.1.0/
    with subdirectories by source and processing status.'
  download_url: https://zenodo.org/records/17235586/files/catalogue.json
  format: JSON (json)
  id: resource_catalogue_json
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Dataset Catalogue
- coordinate_system: null
  description: CSV file providing structured metadata for all datasets in the collection
    including dataset names, descriptions, source attributions, licenses, temporal
    coverage, spatial coverage, and access methods. Lists 18 processed datasets with
    details on agricultural GDP (AgGDP subsectors), demographic data (GHSL population
    and built-up layers), land cover (Copernicus), economic indicators (DOSE-WDI,
    Kummu GDP), infrastructure (GEM power facilities, mining areas), points of interest
    (Overture Maps places and land use), and crop production statistics (MAPSPAM yields).
    Serves as human-readable documentation of the data collection contents and provenance.
  download_url: https://zenodo.org/records/17235586/files/global-spatial-economics-datasets-public.csv
  format: CSV (csv)
  id: resource_metadata_csv
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Dataset Metadata
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-nismod_sdk_regeconactivity
spatial:
  countries:
  - GLO
  scale: global
title: Data to Support Downscaling of Global Regional Economic Activity
version: 0.1.0
vulnerability: null
---
